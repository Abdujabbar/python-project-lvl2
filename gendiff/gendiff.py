import yaml
import json
from collections import defaultdict
from gendiff.constants import ADDED, CHANGED, NESTED, DELETED, SAME


def get_file_contents(path):
    with open(path, 'r') as stream:
        if path.endswith('.json'):

            return json.load(stream)

        return yaml.safe_load(stream)


def detect_operator_and_item(d1, d2, key):
    if key not in d1:
        return (ADDED, [d2.get(key)])

    if key not in d2:
        return (DELETED, [d1.get(key)])

    if isinstance(d1[key], dict) and isinstance(d2[key], dict):
        return (NESTED, [dicts_diff(d1[key], d2[key])])

    if d1.get(key) != d2.get(key):
        return (CHANGED, [d1.get(key), d2.get(key)])

    return (SAME, [d1.get(key)])


def dicts_diff(dict1, dict2):
    all_keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))
    diff_dictionary = defaultdict(tuple)
    for key in all_keys:
        diff_dictionary[key] = detect_operator_and_item(dict1, dict2, key)

    return diff_dictionary


def generate_diff(file1, file2, renderer):
    try:
        content1 = get_file_contents(file1)
        content2 = get_file_contents(file2)
    except Exception as e:
        print(f"Error while reading a file with an exception: {e}")
        exit(0)

    return renderer(dicts_diff(content1, content2))
