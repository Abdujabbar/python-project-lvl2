import yaml
import json

from gendiff.constants import ADDED, CHILD_CHANGED, DELETED, SAME


def get_file_contents(path):
    with open(path, 'r') as stream:
        if path.endswith('.json'):

            return json.load(stream)

        return yaml.safe_load(stream)


def gen_diff_dicts(dict1, dict2): # noqa
    all_keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))
    diff_dictionary = {}
    for key in all_keys:
        if key in dict1.keys() and key in dict2.keys():
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                diff_dictionary[key] = [
                    (CHILD_CHANGED, gen_diff_dicts(dict1[key], dict2[key]))
                ]
                continue

            if dict1.get(key) != dict2.get(key):
                diff_dictionary[key] = [
                    (DELETED, dict1.get(key)),
                    (ADDED, dict2.get(key))
                ]
            else:
                diff_dictionary[key] = [(SAME, dict1.get(key))]
        elif key not in dict1:
            diff_dictionary[key] = [(ADDED, dict2.get(key))]
        elif key not in dict2:
            diff_dictionary[key] = [(DELETED, dict1.get(key))]

    return diff_dictionary


def generate_diff(file1, file2, renderer):
    content1 = get_file_contents(file1)
    dict2 = get_file_contents(file2)

    return renderer(gen_diff_dicts(content1, dict2))
