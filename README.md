# Confirmation Bias Analysis in LLMs

> **MSc Thesis Project** in Computer Science and Engineering – Artificial Intelligence @ Politecnico di Milano.

This repository provides a modular framework for evaluating and quantifying **Confirmation Bias** in Large Language Models (such as GPT, Gemini, and DeepSeek). The evaluation relies on three independent methodologies:

1. **NLI (Natural Language Inference)**: Uses a cross-encoder (`deberta-v3-large`) to detect logical contradictions or entailments between the model's response and the neutral claim.
2. **SAS (Semantic Answer Similarity)**: Measures semantic similarity to check how closely the model's answer aligns with a misleading hint (`stsb-roberta-large`).
3. **LLM-as-a-Judge (GPT)**: Uses a Large Language Model to score how strongly the response sticks to the truth, acting as an independent baseline.

## Project Structure

The project follows a clean and modular architecture:

```text
confirmation-bias-analysis/
│
├── src/                          # Core Python logic (reusable modules)
│   ├── config.py                 # Settings, enabled models, and API keys
│   ├── data_loader.py            # ETL logic for formatting supported datasets
│   ├── llm_client.py             # Target API client (handles retries and parsing)
│   ├── utils.py                  # I/O utilities for streaming reads/writes (JSONL/CSV)
│   ├── final_analysis_utils.py   # Aggregation, plotting, and markdown reporting utilities
│   └── evaluators/               # Independent metric evaluation modules
│       ├── nli.py                # NLI metric implementation
│       ├── sas.py                # SAS metric implementation
│       └── gpt_judge.py          # LLM-as-a-Judge implementation
│
├── notebooks/                    # Notebooks for pipeline execution
│   ├── 01_generation.ipynb       # Queries LLMs and outputs raw .jsonl files
│   ├── 02_evaluation_nli.ipynb   # Calculates NLI metrics
│   ├── 02_evaluation_sas.ipynb   # Calculates SAS metrics
│   ├── 02_evaluation_gpt.ipynb   # Calculates LLM-as-a-Judge metrics
│   └── 03_final_analysis.ipynb   # Aggregates data, computes overall score, and plots results
│
├── data/                         # Input datasets and generated output data
│   ├── raw/                      # Raw .jsonl logs from generation step
│   ├── interim/                  # Intermediate .csv files from each evaluation step
│   └── processed/                # Final merged dataset with all metrics and scores
│
├── pyproject.toml                # Python dependency management
└── README.md                     # This documentation file
```

## Installation & Setup

This project uses a `pyproject.toml` file to handle dependencies cleanly.

**1. Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

**2. Install dependencies:**
Install the project and its requirements in editable mode by running the following command in the root folder:
```bash
pip install -e .
```

**3. Configure API Keys in a `.env` file:**
Create a `.env` file in the repository root. Make sure it stays local and is ignored by git:
```properties
OPENAI_API_KEY="sk-proj-your-openai-api-key"
```

## How to run the pipeline

To do the analysis, run the notebooks in the `notebooks/` folder **in sequential order**:

1. **Configure your targets**: Open `src/config.py` and update the `MODELS_TO_TEST` array with the models you want to evaluate (e.g., `gpt-4o`, `deepseek-r1`).
2. **Generate responses (`notebooks/01_generation.ipynb`)**: This will load the datasets via `data_loader.py` and prompt the active models under three specific conditions (neutral, leading, and contradictory). The raw responses are saved as `.jsonl` logs in the `data/` folder.
3. **Run the evaluations**: The following notebooks process the generated data independently:
   - Run `02_evaluation_nli.ipynb` to extract logical contradictions (NLI).
   - Run `02_evaluation_sas.ipynb` to calculate the semantic shifts caused by the misleading hints (SAS).
   - Run `02_evaluation_gpt.ipynb` to get baseline scores using GPT-4o as a judge.
4. **Final Analysis (`notebooks/03_final_analysis.ipynb`)**: Before running this notebook, open `src/final_analysis_utils.py` and ensure that `DATASETS_TO_COMPARE` and `MODELS_TO_COMPARE` correctly list the evaluated domains to be merged. The notebook then merges the three separate evaluations, calculates the final `CB_OVERALL_SCORE`, generates comparative plots (barplots, heatmaps), and exports aggregated markdown reports.

## Credits & Acknowledgments

This repository contains the source code, data pipelines, and experimental frameworks developed for my MSc Thesis. 

* **Author:** Fabrizio Fontana
* **University:** Politecnico di Milano
* **Degree Program:** MSc in Computer Science and Engineering – Artificial Intelligence
* **Academic Year:** 2025 / 2026
* **Supervisor:** Prof. Cinzia Cappiello
* **Co-Supervisor:** Dott. Mattia Sabella
