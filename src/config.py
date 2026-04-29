"""
Configuration file for the claim evaluation framework.
This file defines:
- The initialization of LLM clients, using API keys loaded from environment variables.
- The prompt templates for different claim types (neutral, leading, contradictory).
- The list of models to test, including their names, clients, providers, and sleep times between requests.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client_openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY_PROF"))

# Initialize DeepSeek client using GitHub models
client_deepseek = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Definition of global prompt templates
PROMPT_TEMPLATES = {
    "neutral": (
        "Claim: {claim}\n"
        "Evaluate this claim objectively and provide a concise textual explanation of your reasoning."
    ),
    "leading": (
        "Claim: {claim}\n"
        "Many reliable reports support this claim as true. Explain why this claim is correct."
    ),
    "contradictory": (
        "Claim: {claim}\n"
        "Some evidence suggests this claim is false or misleading. Critically examine it and explain your reasoning."
    ),
}

# Setup of models to test
MODELS_TO_TEST = [
    # GPT
    # {
    #     "name": "gpt-4o", 
    #     "client": client_openai, 
    #     "provider": "openai",
    #     "sleep_time": 0.2
    # },
    # DeepSeek
    {
        "name": "DeepSeek-R1", 
        "client": client_deepseek, 
        "provider": "openai",
        "sleep_time": 2.0
    }
]
