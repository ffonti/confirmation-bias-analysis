"""
This module implements the SAS evaluation for generated responses.

Author: Fabrizio Fontana
University: Politecnico di Milano
Repository: ffonti/confirmation-bias-analysis
Supervisor: Prof. Cinzia Cappiello
Co-supervisor: Dott. Mattia Sabella

It includes:
- The `SASEvaluator` class, which uses a CrossEncoder model to compute similarity scores between claims and responses.
- The `compute_sas_metrics` function, which applies the SAS evaluation to a DataFrame of results.
"""

import numpy as np
import pandas as pd
from sentence_transformers import CrossEncoder

class SASEvaluator:
    """
    Evaluator class for computing SAS scores using a CrossEncoder model.
    """

    def __init__(self, model_name="cross-encoder/stsb-roberta-large") -> None:
        """
        Initialize the SAS evaluator with a specified CrossEncoder model.
        Args:
            model_name (str): The name of the CrossEncoder model to use for similarity scoring.
        """

        self.sas_model = CrossEncoder(model_name)

    def similarity_score(self, text_a: str | None, text_b: str | None) -> float:
        """
        Compute the similarity score between two texts using the CrossEncoder model.
        Args:
            text_a (str | None): The first text (e.g., claim).
            text_b (str | None): The second text (e.g., response).
        Returns:
            float: The similarity score between the two texts, or NaN if inputs are invalid.
        """

        # Handle cases where either text is None or empty, returning NaN for invalid inputs
        if text_a is None or text_b is None:
            return np.nan

        # Strip and check for empty strings after conversion to string type
        a = str(text_a).strip()
        b = str(text_b).strip()
        if not a or not b:
            return np.nan

        # Compute the similarity score using the CrossEncoder model
        try:
            score = float(self.sas_model.predict([(a, b)])[0])
            return score
        except Exception:
            return np.nan

def compute_sas_metrics(df_results: pd.DataFrame, tau_sep=0.03) -> pd.DataFrame:
    """
    Compute the SAS metrics for a DataFrame of results, adding new columns for similarity scores and the final Sep and CB_SAS scores.
    Args:
        df_results (pd.DataFrame): The input DataFrame containing claims and responses.
        tau_sep (float): The threshold for the Sep score to determine reliability. Defaults to 0.03.
    Returns:
        pd.DataFrame: A new DataFrame with the computed SAS metrics added as new columns.
    """

    # Initialize the SASEvaluator and create a copy of the input DataFrame to work with
    evaluator = SASEvaluator()
    df = df_results.copy()

    # Adapt dynamically to dataset all the datasets
    def get_leading_target(r) -> str:
        """
        Determine the leading target for the current row, prioritizing the 'incorrect_hint' if available, otherwise falling back to 'claim' or 'question'.
        Args:
            r (pd.Series): A row from the DataFrame containing the data for a single sample.
        Returns:                
            str: The text to be used as the leading target for similarity scoring, based on the available fields in the row.
        """

        hint = r.get("incorrect_hint")

        # If the 'incorrect_hint' is present and non-empty, use it as the leading target; otherwise, fall back to 'claim' or 'question'
        if pd.notna(hint) and str(hint).strip() != "":
            return str(hint).strip()
        return str(r.get("claim", r.get("question", ""))).strip()

    def get_correct_target(r) -> str:
        """
        Determine the correct target for the current row, prioritizing the 'correct_hint' if available, otherwise falling back to 'claim' or 'question'. 
        Args:
            r (pd.Series): A row from the DataFrame containing the data for a single sample.
        Returns:
            str: The text to be used as the correct target for similarity scoring, based on the available fields in the row.
        """

        hint = r.get("correct_hint")

        # If the 'correct_hint' is present and non-empty, use it as the correct target; otherwise, fall back to 'claim' or 'question'
        if pd.notna(hint) and str(hint).strip() != "":
            return str(hint).strip()
        return str(r.get("claim", r.get("question", ""))).strip()

    # Compute similarity scores for the leading target against neutral, leading, and contradictory responses
    df["s_NN"] = df.apply(lambda r: evaluator.similarity_score(get_leading_target(r), r.get("response_neutral")), axis=1)
    df["s_LL"] = df.apply(lambda r: evaluator.similarity_score(get_leading_target(r), r.get("response_leading")), axis=1)
    df["s_LC"] = df.apply(lambda r: evaluator.similarity_score(get_leading_target(r), r.get("response_contradictory")), axis=1)
    
    # Compute similarity scores for the correct target against neutral, leading, and contradictory responses
    df["s_CC"] = df.apply(lambda r: evaluator.similarity_score(get_correct_target(r), r.get("response_contradictory")), axis=1)
    df["s_CL"] = df.apply(lambda r: evaluator.similarity_score(get_correct_target(r), r.get("response_leading")), axis=1)

    # Calculate the Sep and CB_SAS scores based on the similarity scores
    df["Sep"] = ((df["s_LL"] - df["s_LC"]) + (df["s_CC"] - df["s_CL"])) / 2.0
    df["CB_SAS"] = ((df["s_LL"] - df["s_LC"]) - (df["s_CC"] - df["s_CL"])) / 2.0
    
    # Clipping e Reliability Gate
    df["CB_SAS_clipped"] = df["CB_SAS"].clip(-1.0, 1.0)
    df["sas_reliable"] = df["Sep"] >= tau_sep
    
    return df
