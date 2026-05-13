import os
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")

DATASETS_TO_COMPARE = ["3_fever", "4_truthfulqa", "5_mmlu_pro"]
MODELS_TO_COMPARE = ["llama3.2", "gemma3", "deepseek_r1_1.5b", "mistral_nemo"]

INTERIM_DATA_DIR = "../data/interim"
BASE_DATA_DIR = "../data/processed"

METRIC_COLUMNS = ["CB_SAS", "CB_NLI", "CB_GPT", "CB_OVERALL"]
SEVERITY_ORDER = ["Null/Low (<= 0.1)", "Moderate (0.1 - 0.5)", "High (> 0.5)"]
FRAMING_ORDER = ["Neutral", "Leading/Conf.", "Contradictory"]

def load_merged_results(dataset_name, model_name):
    safe_model_name = model_name.lower().replace("-", "_").replace(":", "_")
    file_sas = os.path.join(INTERIM_DATA_DIR, dataset_name, safe_model_name, f"{dataset_name}_{safe_model_name}_sas.csv")
    file_nli = os.path.join(INTERIM_DATA_DIR, dataset_name, safe_model_name, f"{dataset_name}_{safe_model_name}_nli.csv")
    file_gpt = os.path.join(INTERIM_DATA_DIR, dataset_name, safe_model_name, f"{dataset_name}_{safe_model_name}_gpt.csv")

    try:
        df_sas = pd.read_csv(file_sas).rename(columns={
            "score_neutral": "sas_score_neutral",
            "score_leading": "sas_score_leading",
            "score_contradictory": "sas_score_contradictory",
        })
        df_nli = pd.read_csv(file_nli).rename(columns={
            "score_neutral": "nli_score_neutral",
            "score_leading": "nli_score_leading",
            "score_contradictory": "nli_score_contradictory",
        })
        df_gpt = pd.read_csv(file_gpt).rename(columns={
            "score_neutral": "gpt_score_neutral",
            "score_leading": "gpt_score_leading",
            "score_contradictory": "gpt_score_contradictory",
        })

        col_nli = "cb_combined" if "cb_combined" in df_nli.columns else "CB_NLI"
        col_sas = "CB_SAS"

        if "CB_GPT" not in df_gpt.columns and {"gpt_score_leading", "gpt_score_contradictory"}.issubset(df_gpt.columns):
            df_gpt["CB_GPT"] = (df_gpt["gpt_score_leading"] - df_gpt["gpt_score_contradictory"]) / 10.0

        nli_cols = ["sample", col_nli] + [c for c in ["nli_score_neutral", "nli_score_leading", "nli_score_contradictory"] if c in df_nli.columns]
        gpt_cols = ["sample", "CB_GPT"] + [c for c in ["gpt_score_neutral", "gpt_score_leading", "gpt_score_contradictory"] if c in df_gpt.columns]

        df_merged = df_sas.merge(df_nli[nli_cols], on="sample", how="inner").merge(df_gpt[gpt_cols], on="sample", how="inner")
        df_merged.rename(columns={col_nli: "CB_NLI", col_sas: "CB_SAS", "CB_GPT": "CB_GPT"}, inplace=True)
        df_merged["CB_OVERALL"] = df_merged[["CB_SAS", "CB_NLI", "CB_GPT"]].mean(axis=1)
        df_merged["dataset"] = dataset_name
        df_merged["model"] = model_name
        return df_merged

    except FileNotFoundError:
        print(f"Missing files for dataset={dataset_name}, model={model_name}. Expected them in {INTERIM_DATA_DIR}/{dataset_name}/{safe_model_name}/")
        return None

def load_and_merge_all_data():
    all_frames = []
    dataset_frames = {}
    model_frames = {}
    
    for dataset_name in DATASETS_TO_COMPARE:
        for model_name in MODELS_TO_COMPARE:
            df_merged = load_merged_results(dataset_name, model_name)
            if df_merged is None:
                continue
            all_frames.append(df_merged)
            dataset_frames.setdefault(dataset_name, []).append(df_merged)
            model_frames.setdefault(model_name, []).append(df_merged)
            print(f"[{dataset_name} | {model_name}] Merge completed on {len(df_merged)} common samples.")

    if all_frames:
        df_all = pd.concat(all_frames, ignore_index=True)
        df_by_dataset = {dataset_name: pd.concat(frames, ignore_index=True) for dataset_name, frames in dataset_frames.items()}
        df_by_model = {model_name: pd.concat(frames, ignore_index=True) for model_name, frames in model_frames.items()}
    else:
        df_all = pd.DataFrame()
        df_by_dataset = {}
        df_by_model = {}

    return df_all, df_by_dataset, df_by_model

def export_results(df_all, df_by_dataset):
    if not df_all.empty:
        os.makedirs(BASE_DATA_DIR, exist_ok=True)
        for dataset_name, df_dataset in df_by_dataset.items():
            output_dataset_file = os.path.join(BASE_DATA_DIR, f"{dataset_name}_cb_overall_analysis.csv")
            df_dataset.to_csv(output_dataset_file, index=False)
            print(f"Saved dataset-level results to {output_dataset_file}")

        combined_output_file = os.path.join(BASE_DATA_DIR, "multi_dataset_cb_overall_analysis.csv")
        df_all.to_csv(combined_output_file, index=False)
        print(f"Saved the combined multi-dataset analysis to {combined_output_file}")
    else:
        print("No data available to export.")


def categorize_bias(score) -> str:
    if pd.isna(score):
        return None
    if score <= 0.1:
        return "Null/Low (<= 0.1)"
    if score <= 0.5:
        return "Moderate (0.1 - 0.5)"
    return "High (> 0.5)"


def ensure_severity_column(df):
    if df.empty:
        return df
    result = df.copy()
    if "Severity" not in result.columns:
        result["Severity"] = result["CB_OVERALL"].apply(categorize_bias)
    return result


def plot_metric_comparison(df_subset, group_col, group_order, title):
    if df_subset.empty:
        print(f"No data available for: {title}")
        return

    ordered_groups = [value for value in group_order if value in df_subset[group_col].unique()]
    mean_scores = df_subset.groupby(group_col)[METRIC_COLUMNS].mean().reset_index()
    melted_scores = mean_scores.melt(id_vars=group_col, var_name="Metric", value_name="Score")

    plt.figure(figsize=(9, 4))
    ax = sns.barplot(data=melted_scores, x="Metric", y="Score", hue=group_col, hue_order=ordered_groups, palette="tab10")
    for patch in ax.patches:
        if pd.notna(patch.get_height()) and patch.get_height() > 0:
            ax.annotate(f"{patch.get_height():.3f}", (patch.get_x() + patch.get_width() / 2., patch.get_height()), ha="center", va="bottom", fontsize=10, color="black", xytext=(0, 5), textcoords="offset points")
    plt.title(title, fontsize=14)
    plt.ylabel("Average Score")
    plt.xlabel("Metric")
    plt.legend(title=group_col.title(), bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()


def plot_severity_distribution(df_subset, group_col, group_order, title):
    if df_subset.empty:
        print(f"No data available for: {title}")
        return

    df_plot = ensure_severity_column(df_subset)
    ordered_groups = [value for value in group_order if value in df_plot[group_col].unique()]
    severity_grouped = (
        df_plot.groupby([group_col, "Severity"]).size().groupby(level=0, group_keys=False).apply(lambda x: 100 * x / x.sum()).reset_index(name="Percentage")
    )

    plt.figure(figsize=(9, 4))
    ax = sns.barplot(data=severity_grouped, x="Severity", y="Percentage", hue=group_col, order=SEVERITY_ORDER, hue_order=ordered_groups, palette="Set2")
    for patch in ax.patches:
        if pd.notna(patch.get_height()) and patch.get_height() > 0:
            ax.annotate(f"{patch.get_height():.1f}%", (patch.get_x() + patch.get_width() / 2., patch.get_height()), ha="center", va="bottom", fontsize=10, color="black", xytext=(0, 5), textcoords="offset points")
    plt.title(title, fontsize=14)
    plt.ylabel("Percentage of Samples (%)")
    plt.xlabel("Severity Level")
    plt.legend(title=group_col.title(), bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()


def build_framing_long(df_subset, x_col):
    if df_subset.empty:
        return pd.DataFrame()

    framing_specs = {
        "SAS": (["sas_score_neutral", "sas_score_leading", "sas_score_contradictory"], lambda s: ((s + 1) / 2.0).clip(0, 1)),
        "NLI": (["nli_score_neutral", "nli_score_leading", "nli_score_contradictory"], lambda s: ((s + 1) / 2.0).clip(0, 1)),
        "GPT": (["gpt_score_neutral", "gpt_score_leading", "gpt_score_contradictory"], lambda s: (s / 10.0).clip(0, 1)),
    }

    rows = []
    for group_value, group_df in df_subset.groupby(x_col):
        for metric_name, (cols, normalizer) in framing_specs.items():
            if all(col in group_df.columns for col in cols):
                means = group_df[cols].mean()
                normalized = normalizer(means)
                for framing_label, col in zip(FRAMING_ORDER, cols):
                    rows.append({x_col: group_value, "Metric": metric_name, "Framing": framing_label, "Score": float(normalized[col])})
    return pd.DataFrame(rows)


def plot_framing_comparison(df_subset, x_col, x_order, title):
    framing_long = build_framing_long(df_subset, x_col)
    if framing_long.empty:
        print(f"No framing data available for: {title}")
        return

    ordered_x = [value for value in x_order if value in framing_long[x_col].unique()]
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    metrics = ["SAS", "NLI", "GPT"]

    for ax, metric in zip(axes, metrics):
        metric_df = framing_long[framing_long["Metric"] == metric]
        if metric_df.empty:
            ax.set_axis_off()
            continue
        sns.barplot(data=metric_df, x=x_col, y="Score", hue="Framing", hue_order=FRAMING_ORDER, order=ordered_x, palette="Set2", ax=ax)
        ax.set_ylim(0, 1.1)
        ax.set_title(metric)
        ax.set_ylabel("Normalized Adherence Score" if metric == "SAS" else "")
        ax.set_xlabel(x_col.title())
        for patch in ax.patches:
            if pd.notna(patch.get_height()) and patch.get_height() > 0:
                ax.annotate(f"{patch.get_height():.2f}", (patch.get_x() + patch.get_width() / 2., patch.get_height()), ha="center", va="bottom", fontsize=9, color="black", xytext=(0, 5), textcoords="offset points")
        if metric != "GPT" and ax.get_legend() is not None:
            ax.get_legend().remove()
        else:
            ax.legend(title="Framing", bbox_to_anchor=(1.05, 1), loc="upper left")

    fig.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()


def plot_heatmap_grid(df_subset, title):
    if df_subset.empty:
        print(f"No heatmap data available for: {title}")
        return

    heatmap_metrics = ["CB_SAS", "CB_NLI", "CB_GPT", "CB_OVERALL"]
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)
    axes = axes.flatten()

    for ax, metric in zip(axes, heatmap_metrics):
        pivot = df_subset.pivot_table(index="dataset", columns="model", values=metric, aggfunc="mean")
        sns.heatmap(pivot, annot=True, fmt=".3f", cmap="coolwarm", ax=ax, cbar=True, vmin=-0.2, vmax=0.50)
        ax.set_title(metric)
        ax.set_xlabel("Model")
        ax.set_ylabel("Dataset")

    fig.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()

