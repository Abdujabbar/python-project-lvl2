import yaml
import json
from gendiff.dicts_diff_generator import generate_dicts_difference
from gendiff.formatters import get_renderer


def get_file_contents(path):
    with open(path, 'r') as stream:
        if path.endswith('.json'):
            return json.load(stream)

        if path.endswith('.yml'):
            return yaml.safe_load(stream)

    raise Exception(f"Unexpected file extension: {path.split('.')[-1]}")


def generate_diff(file1, file2, format='stylish'):
    renderer = get_renderer(format)

    content1 = get_file_contents(file1)
    content2 = get_file_contents(file2)

    return renderer(generate_dicts_difference(content1, content2))
