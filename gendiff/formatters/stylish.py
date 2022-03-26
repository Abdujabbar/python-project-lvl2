INTEND = "    "
LINE_BREAK = "\n"

ADDED_PREFIX = "  + "
DELETED_PREFIX = "  - "
EMPTY_PREFIX = "    "


def render_node(value, pads_count=2):
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
            f"{render_node(v, pads_count + 1)}{LINE_BREAK}"
        )

    result += INTEND * (pads_count - 1) + "}"

    return result


def render_record(depth, key, record):
    method = record.get('action')
    result = ''
    if method == 'record_added':
        result += (
            f"{INTEND * depth}{ADDED_PREFIX}{key}: "
            f"{render_node(record.get('node'), depth + 2)}"
        )

    if method == 'record_deleted':
        result += (
            f"{INTEND * depth}{DELETED_PREFIX}{key}: "
            f"{render_node(record.get('node'), depth + 2)}"
        )

    if method == 'record_changed':
        result += (
            f"{INTEND * depth}{DELETED_PREFIX}{key}: "
            f"{render_node(record.get('old'), depth + 2)}"
        ) + LINE_BREAK
        result += (
            f"{INTEND * depth}{ADDED_PREFIX}{key}: "
            f"{render_node(record.get('new'), depth + 2)}"
        )

    if method == 'record_nested':
        result += (
            f"{INTEND * depth}{EMPTY_PREFIX}{key}: "
            f"{render_helper(record.get('children'), depth + 1)}"
        )

    if method == 'record_same':
        result += (
            f"{INTEND * depth}{EMPTY_PREFIX}{key}: "
            f"{render_node(record.get('node'), depth + 2)}"
        )

    return result


def render_helper(diff_dict, depth=0):
    if not diff_dict:
        return ''

    if not isinstance(diff_dict, dict):
        raise Exception(
            f"Unexpected paramter: {type(diff_dict)}, awaited: dict"
        )

    result = "{" + LINE_BREAK

    for key, record in diff_dict.items():
        result += render_record(depth, key, record) + LINE_BREAK

    result += INTEND * depth + "}"

    return result


def render(diff_dict):
    return render_helper(diff_dict)
