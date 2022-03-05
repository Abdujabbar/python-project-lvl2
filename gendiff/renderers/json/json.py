from gendiff.constants import CHILD_CHANGED, INTEND, LINE_BREAK, PREFIX_MAP


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


def get_prefix(operator):
    return PREFIX_MAP[operator]


def render_dict_item(operator, item, depth):
    if operator == CHILD_CHANGED:
        return render(item, depth + 1)

    return stylish(item, depth + 2)


def render(diff_dict, depth=0):
    result = "{\n"

    for k, items in diff_dict.items():
        for operator, item in items:
            value = render_dict_item(operator, item, depth)
            result += f"{INTEND * depth}{get_prefix(operator)}{k}: {value}\n"

    result += INTEND * depth + "}" + (LINE_BREAK if depth == 0 else '')

    return result
