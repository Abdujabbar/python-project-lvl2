import yaml
import json


def get_file_contents(path, format):
    with open(path, 'r') as stream:
        if format == 'json':

            return json.load(stream)

        return yaml.safe_load(stream)


def generate_diff_dictionaries(content1, content2):
    result = "{\n"
    pads = "    "
    all_keys = sorted(set(list(content1.keys()) + list(content2.keys())))
    for key in all_keys:
        if key in content1 and key in content2:
            if content2[key] != content1[key]:
                result += f"{pads} - {key}: {str(content1.get(key)).lower()}\n"
                result += f"{pads} + {key}: {str(content2.get(key)).lower()}"
            else:
                result += f"{pads}   {key}: {str(content1.get(key)).lower()}"
        elif key not in content1:
            result += f"{pads} - {key}: {str(content2.get(key)).lower()}"
        elif key not in content2:
            result += f"{pads} + {key}: {str(content1.get(key)).lower()}"
        else:
            result += f"{pads}   {key}: {str(content1.get(key)).lower()}"
        result += "\n"
    result += "}\n"

    return result


def generate_diff(file1, file2, format='json'):
    content1 = get_file_contents(file1, format)
    content2 = get_file_contents(file2, format)
    return generate_diff_dictionaries(content1, content2)
