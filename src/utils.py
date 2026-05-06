"""
Utility functions for handling data export operations.

Author: Fabrizio Fontana
University: Politecnico di Milano
Repository: ffonti/confirmation-bias-analysis
Supervisor: Prof. Cinzia Cappiello
Co-supervisor: Dott. Mattia Sabella
"""

import os
import json

def export_to_jsonl(results_list, model_name, dataset_prefix, output_dir="../data/interim") -> str:
    """
    Exports a list of results to a JSONL file, with a structured naming convention based on the model and dataset.
    Args:
        results_list (list): List of dictionaries containing the results to export.
        model_name (str): Name of the model used for generating the results (e.g., "gpt-4o").
        dataset_prefix (str): Prefix for the dataset (e.g., "claims_eval").
        output_dir (str): Directory where the output file will be saved. Defaults to "../data/interim".
    Returns:
        str: The file path of the exported JSONL file.
    """

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Sanitizing the model name
    safe_model_name = model_name.lower().replace("-", "_")
    
    # Building the nested output directory
    target_dir = os.path.join(output_dir, dataset_prefix, safe_model_name)
    os.makedirs(target_dir, exist_ok=True)
    
    # Building the output file path
    output_file = os.path.join(target_dir, f"{dataset_prefix}_{safe_model_name}_results.jsonl")

    # Exporting the results to JSONL
    with open(output_file, 'w', encoding='utf-8') as f:
        for row in results_list:
            json.dump(row, f, ensure_ascii=False)
            f.write('\n')
            
    return output_file
