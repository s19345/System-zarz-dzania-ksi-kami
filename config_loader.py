import json


def load_config(file):
    with open(file) as f:
        return json.load(f)
