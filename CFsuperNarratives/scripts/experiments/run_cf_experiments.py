print(">>> make_cf_tables.py is running", __file__)

import os
import pandas as pd
import sys


# Add the project root (the folder that contains cfsupernarratives_metrics) to sys.path
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from cfsupernarratives_metrics.llm_tools.prompts import build_cf_prompt
from cfsupernarratives_metrics.llm_tools.openai_client import generate_text


# Settings

CF_TABLE_DIR = os.path.join("data", "cf_tables")
RESULTS_DIR = os.path.join("results", "narratives", "adult_rf_long")  # or _short
os.makedirs(RESULTS_DIR, exist_ok=True)

# Which instances to run narratives for (must match those used in make_cf_tables)
INSTANCE_INDICES = [0] # <- change this list as needed

# Choose narrative style
PROMPT_TYPE = "many"  

# Main loop
if __name__ == "__main__":
    for idx in INSTANCE_INDICES:
        cf_path = os.path.join(CF_TABLE_DIR, f"instance_{idx}.csv")
        if not os.path.exists(cf_path):
            print(f"CF table not found for instance {idx}: {cf_path}")
            continue

        print(f"Running CF narrative for instance {idx}...")

        cf_table = pd.read_csv(cf_path, index_col=0)

        # build the full CF prompt
        prompt_text = build_cf_prompt(cf_table, prompt_type=PROMPT_TYPE) #change which prompt to use

        messages = [
            {"role": "system", "content": "You are an expert writer of counterfactual explanations for non-technical users."},
            {"role": "user", "content": prompt_text},
        ]

        # ---- NEW PART: combined table + narrative in one Markdown doc ----
        narrative = generate_text(messages)

        table_md = cf_table.to_markdown(index=True)

        doc_md = f"""# Instance {idx}

## Original instance and counterfactuals

{table_md}

## Counterfactual super narrative

{narrative}
"""

        out_path = os.path.join(RESULTS_DIR, f"instance_{idx}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(doc_md)

        print(f"Saved combined table + narrative to {out_path}")
