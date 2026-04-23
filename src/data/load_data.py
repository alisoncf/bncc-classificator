import json
import pandas as pd

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_csv(path):
    return pd.read_csv(path)