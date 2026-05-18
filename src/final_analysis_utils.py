"""
This module contains utility functions for the final analysis of confirmation bias metrics across multiple datasets and models.

Author: Fabrizio Fontana
University: Politecnico di Milano
Repository: ffonti/confirmation-bias-analysis
Supervisor: Prof. Cinzia Cappiello
Co-supervisor: Dott. Mattia Sabella

It includes:
- `load_merged_results`: Loads and merges SAS, NLI, and GPT results for a given dataset and model.
- `load_and_merge_all_data`: Loads and merges results for all specified datasets and models, returning combined DataFrames.
- `export_results`: Exports aggregated metrics and summaries to a Markdown report.
- `categorize_bias`: Categorizes bias severity based on overall scores.
- `ensure_severity_column`: Ensures the presence of a "Severity" column in the DataFrame.
- `plot_metric_comparison`: Plots average metric scores by a specified grouping column.
- `plot_severity_distribution`: Plots the distribution of bias severity levels by a specified grouping column.
- `build_framing_long`: Builds a long-format DataFrame for framing adherence scores.
- `plot_framing_comparison`: Plots normalized framing adherence scores by dataset and model.
- `plot_heatmap_grid`: Plots a grid of heatmaps for the specified metrics across datasets and models.
"""

import os
import warnings
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")

# Define constants for datasets, models, and directories
DATASETS_TO_COMPARE = ["3_fever", "4_truthfulqa", "5_mmlu_pro"]
MODELS_TO_COMPARE = ["llama3.2", "gemma3", "gpt_4o", "deepseek_r1_1.5b", "mistral_nemo", "phi4", "qwen2.5"]

INTERIM_DATA_DIR = "../data/interim"
BASE_DATA_DIR = "../data/processed"

METRIC_COLUMNS = ["CB_SAS", "CB_NLI", "CB_GPT", "CB_OVERALL"]
SEVERITY_ORDER = ["Null/Low (<= 0.1)", "Moderate (0.1 - 0.5)", "High (> 0.5)"]
FRAMING_ORDER = ["Neutral", "Leading/Conf.", "Contradictory"]

def load_merged_results(dataset_name, model_name) -> pd.DataFrame:
    """
    Loads and merges the SAS, NLI, and GPT results for a given dataset and model.
    Args:
        dataset_name (str): The name of the dataset (e.g., "3_fever").
        model_name (str): The name of the model (e.g., "llama3.2").
    Returns:
        pd.DataFrame: A merged DataFrame containing all metrics for the specified dataset and model, or None if any file is missing.
    """

    # Create safe model name for file paths
    safe_model_name = model_name.lower().replace("-", "_").replace(":", "_")
    file_sas = os.path.join(INTERIM_DATA_DIR, dataset_name, safe_model_name, f"{dataset_name}_{safe_model_name}_sas.csv")
    file_nli = os.path.join(INTERIM_DATA_DIR, dataset_name, safe_model_name, f"{dataset_name}_{safe_model_name}_nli.csv")
    file_gpt = os.path.join(INTERIM_DATA_DIR, dataset_name, safe_model_name, f"{dataset_name}_{safe_model_name}_gpt.csv")

    try:
        # Load and merge the data, handling missing files
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

        # Determine the correct column names for CB_SAS, CB_NLI, and CB_GPT
        col_nli = "cb_combined" if "cb_combined" in df_nli.columns else "CB_NLI"
        col_sas = "CB_SAS"

        # Calculate CB_GPT if not already present, using the difference between leading and contradictory scores normalized to [0, 1]
        if "CB_GPT" not in df_gpt.columns and {"gpt_score_leading", "gpt_score_contradictory"}.issubset(df_gpt.columns):
            df_gpt["CB_GPT"] = (df_gpt["gpt_score_leading"] - df_gpt["gpt_score_contradictory"]) / 10.0

        # Merge on "sample" and keep only the relevant columns for each metric
        nli_cols = ["sample", col_nli] + [c for c in ["nli_score_neutral", "nli_score_leading", "nli_score_contradictory"] if c in df_nli.columns]
        gpt_cols = ["sample", "CB_GPT"] + [c for c in ["gpt_score_neutral", "gpt_score_leading", "gpt_score_contradictory"] if c in df_gpt.columns]

        # Perform inner merge to keep only samples present in all three DataFrames
        df_merged = df_sas.merge(df_nli[nli_cols], on="sample", how="inner").merge(df_gpt[gpt_cols], on="sample", how="inner")
        df_merged.rename(columns={col_nli: "CB_NLI", col_sas: "CB_SAS", "CB_GPT": "CB_GPT"}, inplace=True)
        df_merged["CB_OVERALL"] = df_merged[["CB_SAS", "CB_NLI", "CB_GPT"]].mean(axis=1)
        df_merged["dataset"] = dataset_name
        df_merged["model"] = model_name
        return df_merged

    except FileNotFoundError:
        print(f"Missing files for dataset={dataset_name}, model={model_name}. Expected them in {INTERIM_DATA_DIR}/{dataset_name}/{safe_model_name}/")
        return None

def load_and_merge_all_data() -> (pd.DataFrame, dict, dict): # type: ignore
    """
    Loads and merges results for all datasets and models.
    Returns:
        tuple: A tuple containing the merged DataFrame and dictionaries for each dataset and model.
    """

    all_frames = []
    dataset_frames = {}
    model_frames = {}
    
    for dataset_name in DATASETS_TO_COMPARE:
        for model_name in MODELS_TO_COMPARE:
            # Load and merge results for the current dataset and model
            df_merged = load_merged_results(dataset_name, model_name)
            if df_merged is None:
                continue
            all_frames.append(df_merged)
            dataset_frames.setdefault(dataset_name, []).append(df_merged)
            model_frames.setdefault(model_name, []).append(df_merged)
            print(f"[{dataset_name} | {model_name}] Merge completed on {len(df_merged)} common samples.")

    # Concatenate all frames into a single DataFrame, and also create separate DataFrames for each dataset and model
    if all_frames:
        df_all = pd.concat(all_frames, ignore_index=True)
        df_by_dataset = {dataset_name: pd.concat(frames, ignore_index=True) for dataset_name, frames in dataset_frames.items()}
        df_by_model = {model_name: pd.concat(frames, ignore_index=True) for model_name, frames in model_frames.items()}
    else:
        df_all = pd.DataFrame()
        df_by_dataset = {}
        df_by_model = {}

    return df_all, df_by_dataset, df_by_model

def export_results(df_all, df_by_dataset) -> None:
    """
    Exports aggregated metrics and summaries to a Markdown report, including severity distribution and framing adherence scores.
    Args:
        df_all (pd.DataFrame): The combined DataFrame containing all metrics for all datasets and models.
        df_by_dataset (dict): A dictionary of DataFrames for each dataset, used for severity distribution and framing scores.
    """

    if df_all.empty:
        print("No data available to export.")
        return

    os.makedirs(BASE_DATA_DIR, exist_ok=True)
    output_file = os.path.join(BASE_DATA_DIR, "llm_aggregated_metrics_report.md")

    # Summary by dataset and model
    summary_columns = {metric: ["mean", "std"] for metric in METRIC_COLUMNS}
    summary_by_dataset_model = df_all.groupby(["dataset", "model"]).agg(summary_columns)
    summary_by_dataset_model.columns = [f"{m}_{s}" for m, s in summary_by_dataset_model.columns]

    # Summary by dataset
    summary_by_dataset = df_all.groupby("dataset").agg(summary_columns)
    summary_by_dataset.columns = [f"{m}_{s}" for m, s in summary_by_dataset.columns]

    # Summary by model
    summary_by_model = df_all.groupby("model").agg(summary_columns)
    summary_by_model.columns = [f"{m}_{s}" for m, s in summary_by_model.columns]

    # Severity Distribution
    df_severity = ensure_severity_column(df_all)
    severity_counts = df_severity.groupby(["dataset", "model", "Severity"]).size().reset_index(name="Count")
    total_counts = severity_counts.groupby(["dataset", "model"])["Count"].transform("sum")
    severity_counts["Percentage"] = 100 * severity_counts["Count"] / total_counts

    # Framing Scores
    framing_specs = {
        "SAS": (["sas_score_neutral", "sas_score_leading", "sas_score_contradictory"], lambda s: ((s + 1) / 2.0).clip(0, 1)),
        "NLI": (["nli_score_neutral", "nli_score_leading", "nli_score_contradictory"], lambda s: ((s + 1) / 2.0).clip(0, 1)),
        "GPT": (["gpt_score_neutral", "gpt_score_leading", "gpt_score_contradictory"], lambda s: (s / 10.0).clip(0, 1)),
    }
    rows = []

    # Iterate over each dataset and model group to calculate mean framing scores and normalize them
    for (ds, mod), group_df in df_all.groupby(["dataset", "model"]):
        for metric_name, (cols, normalizer) in framing_specs.items():
            if all(col in group_df.columns for col in cols):
                means = group_df[cols].mean()
                normalized = normalizer(means)
                for framing_label, col in zip(FRAMING_ORDER, cols):
                    rows.append({"dataset": ds, "model": mod, "Metric": metric_name, "Framing": framing_label, "Score": float(normalized[col])})
    
    framing_res = pd.DataFrame(rows) if rows else pd.DataFrame()

    # Write the report to a Markdown file, including all summaries and the severity distribution and framing adherence scores
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Aggregated Confirmation Bias Metrics Report\n\n")
        f.write("## 1. Overall Summary (Dataset & Model)\n")
        f.write(summary_by_dataset_model.to_markdown())
        f.write("\n\n## 2. Summary by Dataset\n")
        f.write(summary_by_dataset.to_markdown())
        f.write("\n\n## 3. Summary by Model\n")
        f.write(summary_by_model.to_markdown())
        f.write("\n\n## 4. Severity Distribution (Dataset & Model)\n")
        f.write(severity_counts.to_markdown(index=False))
        f.write("\n\n")
        if not framing_res.empty:
            f.write("## 5. Normalized Framing Adherence Score (Dataset & Model)\n")
            f.write(framing_res.to_markdown(index=False))
            f.write("\n")

    print(f"Saved aggregated LLM report to {output_file}")

def categorize_bias(score) -> str:
    """
    Categorizes bias severity based on overall scores.
    Args:
        score (float): The overall bias score to categorize.
    Returns:
        str: The severity category.
    """

    if pd.isna(score):
        return None
    if score <= 0.1:
        return "Null/Low (<= 0.1)"
    if score <= 0.5:
        return "Moderate (0.1 - 0.5)"
    return "High (> 0.5)"

def ensure_severity_column(df) -> pd.DataFrame:
    """
    Ensures the presence of a "Severity" column in the DataFrame, categorizing bias severity based on overall scores.
    Args:
        df (pd.DataFrame): The input DataFrame containing at least the "CB_OVERALL" column.
    Returns:
        pd.DataFrame: The DataFrame with an added "Severity" column if it was not already present.
    """

    if df.empty:
        return df
    result = df.copy()
    if "Severity" not in result.columns:
        result["Severity"] = result["CB_OVERALL"].apply(categorize_bias)
    return result

def plot_metric_comparison(df_subset, group_col, group_order, title) -> None:
    """
    Plots average metric scores by a specified grouping column (e.g., dataset or model), showing the mean scores for CB_SAS, CB_NLI, CB_GPT, and CB_OVERALL.
    Args:
        df_subset (pd.DataFrame): The subset of the DataFrame to plot, containing the relevant metrics and grouping column.
        group_col (str): The name of the column to group by (e.g., "dataset" or "model").
        group_order (list): The desired order of the groups for consistent coloring and presentation.
        title (str): The title of the plot to display at the top of the figure.
    """

    if df_subset.empty:
        print(f"No data available for: {title}")
        return

    # Filter the group order to include only groups present in the data
    ordered_groups = [value for value in group_order if value in df_subset[group_col].unique()]
    mean_scores = df_subset.groupby(group_col)[METRIC_COLUMNS].mean().reset_index()
    melted_scores = mean_scores.melt(id_vars=group_col, var_name="Metric", value_name="Score")

    # Create a bar plot comparing the average scores for each metric across the specified groups
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

def plot_severity_distribution(df_subset, group_col, group_order, title) -> None:
    """
    Plots the distribution of bias severity levels by a specified grouping column (e.g., dataset or model), showing the percentage of samples in each severity category.
    Args:
        df_subset (pd.DataFrame): The subset of the DataFrame to plot, containing the "Severity" column and the grouping column.
        group_col (str): The name of the column to group by (e.g., "dataset" or "model").
        group_order (list): The desired order of the groups for consistent coloring and presentation.
        title (str): The title of the plot to display at the top of the figure.
    """

    if df_subset.empty:
        print(f"No data available for: {title}")
        return

    # Ensure the "Severity" column is present and categorized, then calculate the percentage distribution of severity levels for each group
    df_plot = ensure_severity_column(df_subset)
    ordered_groups = [value for value in group_order if value in df_plot[group_col].unique()]
    severity_grouped = (
        df_plot.groupby([group_col, "Severity"]).size().groupby(level=0, group_keys=False).apply(lambda x: 100 * x / x.sum()).reset_index(name="Percentage")
    )

    # Create a bar plot showing the percentage of samples in each severity category for each group
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

def build_framing_long(df_subset, x_col) -> pd.DataFrame:
    """
    Builds a long-format DataFrame for framing adherence scores, calculating mean scores for each framing type and normalizing them to a [0, 1] scale for comparison across metrics.
    Args:
        df_subset (pd.DataFrame): The subset of the DataFrame containing the relevant framing score columns and the grouping column.
        x_col (str): The name of the column to group by (e.g., "dataset" or "model").
    Returns:
        pd.DataFrame: A long-format DataFrame with columns for the grouping variable, metric name, framing type, and normalized score, suitable for plotting.
    """
    if df_subset.empty:
        return pd.DataFrame()

    # Define the specifications for each metric, including the relevant columns for each framing type and the normalization function to convert scores to a [0, 1] scale
    framing_specs = {
        "SAS": (["sas_score_neutral", "sas_score_leading", "sas_score_contradictory"], lambda s: ((s + 1) / 2.0).clip(0, 1)),
        "NLI": (["nli_score_neutral", "nli_score_leading", "nli_score_contradictory"], lambda s: ((s + 1) / 2.0).clip(0, 1)),
        "GPT": (["gpt_score_neutral", "gpt_score_leading", "gpt_score_contradictory"], lambda s: (s / 10.0).clip(0, 1)),
    }

    # Iterate over each group defined by the grouping column, calculate mean scores for each framing type and metric, normalize them, and build a long-format DataFrame for plotting
    rows = []
    for group_value, group_df in df_subset.groupby(x_col):
        for metric_name, (cols, normalizer) in framing_specs.items():
            if all(col in group_df.columns for col in cols):
                means = group_df[cols].mean()
                normalized = normalizer(means)
                for framing_label, col in zip(FRAMING_ORDER, cols):
                    rows.append({x_col: group_value, "Metric": metric_name, "Framing": framing_label, "Score": float(normalized[col])})
    return pd.DataFrame(rows)

def plot_framing_comparison(df_subset, x_col, x_order, title) -> None:
    """
    Plots normalized framing adherence scores by dataset and model, showing the mean scores for each framing type (Neutral, Leading/Conf., Contradictory) across the specified grouping variable (e.g., dataset or model).
    Args:
        df_subset (pd.DataFrame): The subset of the DataFrame containing the relevant framing score columns and the grouping column.
        x_col (str): The name of the column to group by (e.g., "dataset" or "model").
        x_order (list): The desired order of the groups for consistent coloring and presentation.
        title (str): The title of the plot to display at the top of the figure.
    """
    
    # Build a long-format DataFrame for framing adherence scores, calculating mean scores for each framing type and normalizing them to a [0, 1] scale for comparison across metrics
    framing_long = build_framing_long(df_subset, x_col)
    if framing_long.empty:
        print(f"No framing data available for: {title}")
        return

    # Filter the x-axis order to include only groups present in the data
    ordered_x = [value for value in x_order if value in framing_long[x_col].unique()]
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    metrics = ["SAS", "NLI", "GPT"]

    # Create a bar plot for each metric, comparing the normalized framing adherence scores for each framing type across the specified groups, and annotate the bars with the exact score values
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

def plot_heatmap_grid(df_subset, title) -> None:
    """
    Plots a grid of heatmaps for the specified metrics (CB_SAS, CB_NLI, CB_GPT, CB_OVERALL) across datasets and models, showing the mean scores for each metric in a 2x2 layout.
    Args:
        df_subset (pd.DataFrame): The subset of the DataFrame containing the relevant metrics and grouping columns for datasets and models.
        title (str): The title of the plot to display at the top of the figure.
    """

    if df_subset.empty:
        print(f"No heatmap data available for: {title}")
        return

    # Define the metrics to include in the heatmaps, then create a 2x2 grid of heatmaps showing the mean scores for each metric across datasets and models
    heatmap_metrics = ["CB_SAS", "CB_NLI", "CB_GPT", "CB_OVERALL"]
    fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)
    axes = axes.flatten()

    # For each metric, create a pivot table of mean scores by dataset and model, then plot a heatmap with consistent color scaling across all metrics for easy comparison, and annotate the heatmap cells with the exact mean score values
    for ax, metric in zip(axes, heatmap_metrics):
        pivot = df_subset.pivot_table(index="dataset", columns="model", values=metric, aggfunc="mean")
        sns.heatmap(pivot, annot=True, fmt=".3f", cmap="coolwarm", ax=ax, cbar=True, vmin=-0.2, vmax=0.50)
        ax.set_title(metric)
        ax.set_xlabel("Model")
        ax.set_ylabel("Dataset")

    fig.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()
