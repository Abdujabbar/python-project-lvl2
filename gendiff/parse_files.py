import json
import yaml


def get_file_contents(path):
    with open(path, 'r') as stream:
        if path.endswith('.json'):

            return json.load(stream)

        return yaml.safe_load(stream)
