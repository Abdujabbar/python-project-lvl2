from gendiff.constants import INTEND


def stylish(value, pads_count=2):
    if value is None:
        return 'null'

    if isinstance(value, str):
        return value

    if not isinstance(value, dict):
        return str(value).lower()

    result = "{\n"

    for k, v in value.items():
        result += f"{INTEND * pads_count}{k}: {stylish(v, pads_count + 1)}\n"

    result += INTEND * (pads_count - 1) + "}"

    return result
