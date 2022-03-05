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


def render(diff_dictionary, depth=0):
    result = "{\n"

    for k, items in diff_dictionary.items():
        for v in items:
            operator = v[0]
            prefix = PREFIX_MAP[operator]

            if operator == CHILD_CHANGED:
                value = render(v[1], depth + 1)
            else:
                value = stylish(v[1], depth + 2)

            result += f"{INTEND * depth}{prefix}{k}: {value}\n"

    result += INTEND * depth + "}"
    if depth == 0:
        result += LINE_BREAK

    return result
