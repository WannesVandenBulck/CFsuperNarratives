# cfsupernarratives_metrics/llm_tools/openai_client.py

import yaml
from openai import OpenAI


# --- Load API key from YAML ---
with open("config/keys.yaml", "r") as f:
    KEYS = yaml.safe_load(f)

api_key = KEYS["openai_key"]


# --- Create OpenAI client (new v1+ API) ---
client = OpenAI(api_key=api_key)


def generate_text(messages, model="gpt-5.1", temperature=0):
    """
    Generate text using the new OpenAI v1+ Chat Completions API.
    messages must be a list of {"role": ..., "content": ...}.
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

