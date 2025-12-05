import pandas as pd
from cfsupernarratives_metrics.llm_tools.prompts import build_cf_prompt
from cfsupernarratives_metrics.llm_tools.openai_client import generate_text

class CFExperiment:
    def __init__(self, config):
        self.config = config

    def run_single(self, instance_id):
        cf_table_path = f"data/cf_tables/{instance_id}.csv"
        cf_table = pd.read_csv(cf_table_path, index_col=0)

        prompt = build_cf_prompt(cf_table, long=self.config["long"])

        narrative = generate_text([
            {"role": "system", "content": "You are an expert writer of counterfactual explanations."},
            {"role": "user", "content": prompt},
        ])

        out_path = f"results/narratives/{self.config['name']}/{instance_id}.txt"
        with open(out_path, "w") as f:
            f.write(narrative)

        return narrative
