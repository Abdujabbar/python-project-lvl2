import yaml
import json

from gendiff.constants import SMALL_INTEND
from gendiff.constants import INTEND
from gendiff.constants import LINE_BREAK
from gendiff.constants import DIFF_LINE_MINUS
from gendiff.constants import DIFF_LINE_PLUS
from gendiff.formatter import stylish


def get_file_contents(path, format):
    with open(path, 'r') as stream:
        if format == 'json':

            return json.load(stream)

        return yaml.safe_load(stream)



def generate_diff_dictionaries(content1, content2, pads_count = 1):
    result = "{\n"
    all_keys = sorted(set(list(content1.keys()) + list(content2.keys())))

    for key in all_keys:
        if key in content1 and key in content2:
            if content2[key] != content1[key]:
                if isinstance(content2[key], dict) and isinstance(content2[key], dict):
                    result += f"{INTEND * pads_count}{key}: " + generate_diff_dictionaries(content1.get(key), content2.get(key), pads_count + 1)
                else:
                    result += f"{INTEND * (pads_count - 1)}{DIFF_LINE_MINUS}{key}: {stylish(content1.get(key), pads_count + 1)}\n"
                    result += f"{INTEND * (pads_count - 1)}{DIFF_LINE_PLUS}{key}: {stylish(content2.get(key), pads_count + 1)}"
            else:
                result += f"{INTEND * pads_count}{key}: {stylish(content1.get(key), pads_count + 1)}"
        elif key not in content1:
            result += f"{INTEND * (pads_count - 1)}{DIFF_LINE_PLUS}{key}: {stylish(content2.get(key), pads_count + 1)}"
        elif key not in content2:
            result += f"{INTEND * (pads_count - 1)}{DIFF_LINE_MINUS}{key}: {stylish(content1.get(key), pads_count + 1)}"
        else:
            result += f"{INTEND * pads_count}{key}: {stylish(content1.get(key), pads_count + 1)}"
        result += "\n"
    result += INTEND * (pads_count - 1) + "}"

    if pads_count == 1:
        result += "\n"
    
    return result


def generate_diff(file1, file2, format='json'):
    content1 = get_file_contents(file1, format)
    content2 = get_file_contents(file2, format)
    return generate_diff_dictionaries(content1, content2)
