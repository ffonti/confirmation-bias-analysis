"""
NLI Evaluator for computing entailment and contradiction scores.
This module includes:
- The `NLIEvaluator` class, which uses a CrossEncoder model to compute alignment scores between claims and responses.
- The `compute_nli_metrics` function, which applies the NLI evaluation to a DataFrame of results and computes various confirmation bias metrics based on the alignment scores.
"""

import numpy as np
import pandas as pd
from sentence_transformers import CrossEncoder

class NLIEvaluator:
    """
    Evaluator class for computing NLI-based alignment scores using a CrossEncoder model.
    """

    def __init__(self, model_name="cross-encoder/nli-deberta-v3-large") -> None:
        """
        Initialize the NLI evaluator with a specified CrossEncoder model.
        Args:
            model_name (str): The name of the CrossEncoder model to use for NLI scoring.
        """

        # Initialize the CrossEncoder model and create a mapping from label indices to their corresponding labels
        self.nli_model = CrossEncoder(model_name)
        self.id2label = {int(k): str(v).lower() for k, v in self.nli_model.model.config.id2label.items()}
        
        # Identify the indices for the "contradiction" and "entailment" labels based on the model's label mapping
        self.contradiction_idx = self._label_index("contradiction")
        self.entailment_idx = self._label_index("entailment")

    def _label_index(self, keyword) -> int:
        """
        Find the index of a label in the model's label mapping based on a keyword.
        Args:
            keyword (str): The keyword to search for in the label names (e.g., "contradiction" or "entailment").
        Returns:
            int: The index of the label in the model's label mapping.
        """

        # Search for the label index that contains the specified keyword, ignoring case, and return it
        for idx, label in self.id2label.items():
            if keyword in label:
                return idx
        raise ValueError(f"Label '{keyword}' not found in model labels: {self.id2label}")

    def _softmax(self, logits) -> np.ndarray:
        """
        Compute the softmax of a list of logits to convert them into probabilities.
        Args:
            logits (list): A list of raw output scores from the model for each class.
        Returns:
            np.ndarray: An array of probabilities corresponding to each class, summing to 1.
        """

        # Compute the softmax of the logits to get probabilities for each class
        x = np.asarray(logits, dtype=float)
        x = x - np.max(x)
        exp_x = np.exp(x)
        return exp_x / exp_x.sum()

    def alignment_score(self, premise, hypothesis) -> float | None:
        """
        Calculate the alignment score between a premise and a hypothesis.
        Args:
            premise (str): The premise sentence.
            hypothesis (str): The hypothesis sentence.
        Returns:
            float | None: The alignment score, or None if either input is invalid.
        """

        if premise is None or hypothesis is None:
            return None

        # Strip and check for empty strings after conversion to string type, returning None for invalid inputs
        p = str(premise).strip()
        h = str(hypothesis).strip()
        if p == "" or h == "":
            return None

        # Compute the logits from the NLI model for the given premise and hypothesis, convert them to probabilities
        logits = self.nli_model.predict([(p, h)])[0]
        probs = self._softmax(logits)
        
        # Calculate the alignment score as the difference between the entailment and contradiction probabilities
        return float(probs[self.entailment_idx] - probs[self.contradiction_idx])

def compute_nli_metrics(df_results: pd.DataFrame) -> pd.DataFrame:
    """
    Compute the NLI-based metrics for a DataFrame of results, adding new columns for the alignment scores and the final confirmation bias scores.
    Args:
        df_results (pd.DataFrame): The input DataFrame containing claims and responses.
    Returns:
        pd.DataFrame: A new DataFrame with the computed NLI metrics added as new columns.
    """
    
    evaluator = NLIEvaluator()
    combined_bias_values = []
    
    # Create a copy of the input DataFrame to work with and initialize new columns for the NLI scores and confirmation bias metrics
    df = df_results.copy()
    
    # Iterate over each row in the DataFrame and compute the NLI alignment scores for the neutral and contradictory responses
    for index, row in df.iterrows():
        claim = row["claim"]
        r_neut = row["response_neutral"]
        r_lead = row["response_leading"]
        r_contra = row["response_contradictory"]
        
        # Compute the NLI alignment scores for the neutral and contradictory responses against the claim
        s_neut_claim = evaluator.alignment_score(claim, r_neut)
        s_contra_claim = evaluator.alignment_score(claim, r_contra)
        
        # Stance Shift: difference between the alignment of the neutral response and the contradictory response to the claim
        cb_shift_i = (s_neut_claim - s_contra_claim) / 2.0 if s_neut_claim is not None and s_contra_claim is not None else np.nan
        
        # Self-Confirmation: difference between the alignment of the neutral response to the claim and the alignment of the leading response to the claim
        d_lead = evaluator.alignment_score(r_neut, r_lead)
        d_contra = evaluator.alignment_score(r_neut, r_contra)
        cb_self_i = (d_lead - d_contra) / 2.0 if d_lead is not None and d_contra is not None else np.nan
        
        # Combined Bias: average of the Stance Shift and Self-Confirmation scores, clipped to the range [-1.0, 1.0], or NaN if either score is invalid
        if pd.notna(cb_shift_i) and pd.notna(cb_self_i):
            cb_combined_i = (cb_shift_i + cb_self_i) / 2.0
            combined_bias_value = float(np.clip(cb_combined_i, -1.0, 1.0))
        else:
            combined_bias_value = np.nan
        
        # Append the computed combined bias value to the list for potential further analysis or export
        combined_bias_values.append(combined_bias_value)
        
        # Add the computed NLI scores and confirmation bias metrics to the DataFrame for the current row
        df.at[index, "nli_s_neut_claim"] = s_neut_claim
        df.at[index, "nli_s_contra_claim"] = s_contra_claim
        df.at[index, "cb_shift"] = cb_shift_i
        df.at[index, "cb_self"] = cb_self_i
        df.at[index, "cb_combined"] = combined_bias_value

    return df
