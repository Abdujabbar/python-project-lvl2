INTEND = "    "
LINE_BREAK = "\n"

ADDED_PREFIX = "  + "
DELETED_PREFIX = "  - "
EMPTY_PREFIX = "    "


def render_value(value, pads_count=2):
    if value is None:
        return 'null'

    if isinstance(value, str):
        return value

    if not isinstance(value, dict):
        return str(value).lower()

    result = "{\n"

    for k, v in value.items():
        result += (
            f"{INTEND * pads_count}{k}: "
            f"{render_value(v, pads_count + 1)}{LINE_BREAK}"
        )

    result += INTEND * (pads_count - 1) + "}"

    return result


def record_added(depth, key, value):
    return (
        f"{INTEND * depth}{ADDED_PREFIX}{key}: "
        f"{render_value(value, depth + 2)}"
    )


def record_deleted(depth, key, value):
    return (
        f"{INTEND * depth}{DELETED_PREFIX}{key}: "
        f"{render_value(value, depth + 2)}"
    )


def record_changed(depth, key, old_value, new_value):
    result = ""
    result += record_deleted(depth, key, old_value) + LINE_BREAK
    result += record_added(depth, key, new_value)
    return result


def record_nested(depth, key, value):
    return f"{INTEND * depth}{EMPTY_PREFIX}{key}: {render(value, depth + 1)}"


def record_same(depth, key, value):
    return (
        f"{INTEND * depth}{EMPTY_PREFIX}{key}: "
        f"{render_value(value, depth + 2)}"
    )


def render(diff_dict, depth=0):
    result = "{" + LINE_BREAK

    for key, value in diff_dict.items():
        method = value.get('method')
        item = value.get('item')
        result += globals()[method](*[depth, key, *item]) + LINE_BREAK

    result += INTEND * depth + "}"

    return result
