"""
LLM Client module for querying language models and managing the generation pipeline.

Author: Fabrizio Fontana
University: Politecnico di Milano
Repository: ffonti/confirmation-bias-analysis
Supervisor: Prof. Cinzia Cappiello
Co-supervisor: Dott. Mattia Sabella

This module includes:
- The `query_llm` function, which sends prompts to the configured LLMs and handles responses, including retry logic for rate limits.
- The `run_generation_pipeline` function, which iterates through a dataset, queries multiple LLMs for each sample, and saves results progressively using the export utility.
"""

import os
import json
import time
import re
from src.utils import export_to_jsonl

def query_llm(prompt, model_config) -> str:
    """
    Sends a prompt to the specified LLM and returns the response, with retry logic for rate limits.
    Args:
        prompt (str): The prompt to send to the LLM.
        model_config (dict): Configuration dictionary for the model, containing keys like "name", "client", and "provider".
    Returns:
        str: The response from the LLM, or None if an error occurs.
    """
    
    # System message to guide the LLM's response format
    system_msg = (
        "Provide a concise textual explanation (3-5 sentences). "
        "Do not answer with only a label or single letter."
    )

    # Extracting model details from the configuration
    client = model_config["client"]
    model_name = model_config["name"]
    provider = model_config["provider"]
    
    # Retry logic parameters
    max_retries = 3

    # Attempt to query the LLM, with retries for rate limits
    for attempt in range(max_retries):
        try:
            if provider == "openai":
                # Querying the model using the OpenAI client interface
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": system_msg},
                        {"role": "user", "content": prompt}
                    ],
                    stream=False
                )

                # Extracting and cleaning the response text
                text = response.choices[0].message.content.strip()
                
                # Removing any <think>...</think> tags and their content if present (usually in DeepSeek responses)
                text = re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL)

                return text
                
            elif provider == "gemini":
                # Querying the model using the Gemini client interface
                model = client.GenerativeModel(model_name)
                response = model.generate_content(system_msg + "\n\n" + prompt)

                # Extracting and cleaning the response text
                text = response.text.strip()

                # Removing any <think>...</think> tags and their content if present (if Gemini uses similar formatting)
                text = re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL)
                return text

            return None
  
        except Exception as e:
            error_str = str(e)

            # Check for rate limit errors and extract wait time if specified
            if "429" in error_str or "Rate limit" in error_str or "RateLimitReached" in error_str:

                # Attempt to extract wait time from the error message (e.g., "wait 60 seconds")
                match = re.search(r'wait (\d+) seconds', error_str)
                if match:
                    wait_time = int(match.group(1))
                    
                    # Convert wait time to a more human-readable format for logging
                    hours = wait_time // 3600
                    minutes = (wait_time % 3600) // 60
                    seconds = wait_time % 60
                    time_formatted = f"{hours}h {minutes}m {seconds}s" if hours > 0 else f"{minutes}m {seconds}s"
                    
                    # If the wait time is excessively long (e.g., more than 5 minutes), we can assume it's a daily limit and stop retrying for this model
                    if wait_time > 300: 
                        print(f"[{model_name}] Daily limit reached. Required time: {time_formatted} ({wait_time}s). Safe interruption for this model.")
                        return "DAILY_LIMIT_REACHED"
                    
                    # Else, we wait for the specified time and retry
                    print(f"[{model_name}] Rate limit exceeded. Waiting for {time_formatted}... (Attempt {attempt+1}/{max_retries})")
                    time.sleep(wait_time + 1)

                    continue
                else:
                    # Generic rate limit error without specified wait time, we can wait 60 seconds before retrying
                    print(f"[{model_name}] Generic rate limit error. Waiting 60s and retrying...")
                    time.sleep(60)

                    continue
            
            # If it's a different error, we log it and return None
            print(f"Error for {model_name}: {e}")

            return None
            
    # If we exhaust all retries without success, we log the failure and treat as DAILY LIMIT
    print(f"[{model_name}] Impossible to process the request after {max_retries} attempts. Assuming severe exhaustion.")

    return "DAILY_LIMIT_REACHED"

def run_generation_pipeline(dataset_df, models_config, output_prefix, output_dir="../data/interim") -> list:
    """Runs the generation pipeline by iterating through the dataset and querying each model for each sample, saving results progressively.
    Args:
        dataset_df (pd.DataFrame): The input dataset containing claims and prompts.
        models_config (list): List of model configuration dictionaries to test.
        output_prefix (str): Prefix for the output files (e.g., "claims_eval")."
        output_dir (str): Directory where the output files will be saved.
    Returns:
        list: A list of file paths for the saved JSONL files corresponding to each model.
    """

    print(f"Starting the querying process for {len(dataset_df)} samples on {len(models_config)} models...\n")
    
    # List to keep track of all saved file paths for final output
    all_saved_files = []
    
    # Iterating through each model
    for model_config in models_config:
        model_name = model_config["name"]
        delay = model_config.get("sleep_time", 1.0) 
        print(f"--- Starting test for model: {model_name} ---")
        
        # List to accumulate results for the current model, which will be saved progressively
        results_list = []
        
        # Check for existing results to resume
        safe_model_name = model_name.lower().replace("-", "_")
        expected_output_file = os.path.join(output_dir, f"{output_prefix}_{safe_model_name}_results.jsonl")
        
        # Set to keep track of already processed samples to avoid duplication when resuming
        processed_samples = set()
        if os.path.exists(expected_output_file):
            with open(expected_output_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        data = json.loads(line)
                        results_list.append(data)
                        processed_samples.add(data.get("sample"))
            print(f"Resuming from {len(processed_samples)} previously saved samples...")

        # Iterating through each sample in the dataset
        for index, row in dataset_df.iterrows():
            if (index + 1) in processed_samples:
                continue

            print(f"Sample {index+1}/{len(dataset_df)} (Model: {model_name})")
            
            # Querying the LLM for each prompt type (neutral, leading, contradictory) and handling rate limits
            response_neutral = query_llm(row["prompt_neutral"], model_config)
            if response_neutral in ["DAILY_LIMIT_REACHED", None]: break
            time.sleep(delay)

            response_leading = query_llm(row["prompt_leading"], model_config)
            if response_leading in ["DAILY_LIMIT_REACHED", None]: break
            time.sleep(delay)

            response_contradictory = query_llm(row["prompt_contradictory"], model_config)
            if response_contradictory in ["DAILY_LIMIT_REACHED", None]: break
            time.sleep(delay)

            # Extracting the claim text for the result entry, handling both "claim" and "premise" cases
            claim_text = row["claim"] if "claim" in row else row.get("premise", "")
            
            # Building the result entry for the current sample and model
            result_entry = {
                "sample": index + 1,
                "model": model_name,
                "claim": claim_text,
                "response_neutral": response_neutral,
                "response_leading": response_leading,
                "response_contradictory": response_contradictory,
            }
            
            # If the original dataset has a "label" column, we include it in the result entry for reference
            if "label" in row:
                result_entry["label"] = row["label"]
            
            results_list.append(result_entry)
            
            # Progressive saving (overwrites the file as it updates, ensuring we always have the latest results even if the process is interrupted)
            export_to_jsonl(results_list, model_name, output_prefix, output_dir=output_dir)

        print(f"--- Test completed (or interrupted at the limit) for: {model_name} ---\n")
        
        # Reapply the last export to obtain with certainty the final path and paste it in output
        saved_file = export_to_jsonl(results_list, model_name, output_prefix, output_dir=output_dir)
        all_saved_files.append(saved_file)
        
    print("All generation pipelines are completed.")
    
    return all_saved_files
