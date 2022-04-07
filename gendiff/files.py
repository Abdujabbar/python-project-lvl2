import json
import yaml


def parse_content(path):
    with open(path, 'r') as stream:
        if path.endswith('.json'):
            return json.load(stream)

        if path.endswith('.yml') or path.endswith('.yaml'):
            return yaml.safe_load(stream)

    raise Exception(f"Unexpected file extension: {path.split('.')[-1]}")
