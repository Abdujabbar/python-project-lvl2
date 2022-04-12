INTEND = "    "
LINE_BREAK = "\n"

ADDED_PREFIX = "  + "
DELETED_PREFIX = "  - "
EMPTY_PREFIX = "    "


def to_string(value, pads_count=2):
    if value is None:
        return 'null'

    if isinstance(value, str):
        return value

    if not isinstance(value, dict):
        return str(value).lower()

    result = "{" + LINE_BREAK

    for k, v in value.items():
        result += (
            f"{INTEND * pads_count}{k}: "
            f"{to_string(v, pads_count + 1)}{LINE_BREAK}"
        )

    result += INTEND * (pads_count - 1) + "}"

    return result


def convert_record_to_string(record, depth, key):
    method = record.get('action')
    result = ''
    if method == 'record_added':
        result += (
            f"{INTEND * depth}{ADDED_PREFIX}{key}: "
            f"{to_string(record.get('value'), depth + 2)}"
        )

    if method == 'record_deleted':
        result += (
            f"{INTEND * depth}{DELETED_PREFIX}{key}: "
            f"{to_string(record.get('value'), depth + 2)}"
        )

    if method == 'record_changed':
        result += (
            f"{INTEND * depth}{DELETED_PREFIX}{key}: "
            f"{to_string(record.get('old'), depth + 2)}"
        ) + LINE_BREAK
        result += (
            f"{INTEND * depth}{ADDED_PREFIX}{key}: "
            f"{to_string(record.get('new'), depth + 2)}"
        )

    if method == 'record_nested':
        result += (
            f"{INTEND * depth}{EMPTY_PREFIX}{key}: "
            f"{crawl(record.get('children'), depth + 1)}"
        )

    if method == 'record_same':
        result += (
            f"{INTEND * depth}{EMPTY_PREFIX}{key}: "
            f"{to_string(record.get('value'), depth + 2)}"
        )

    return result


def crawl(diff_dict, depth=0):
    if not diff_dict:
        return ''

    if not isinstance(diff_dict, dict):
        raise Exception(
            f"Unexpected paramter: {type(diff_dict)}, awaited: dict"
        )

    result = "{" + LINE_BREAK

    for key, record in diff_dict.items():
        result += convert_record_to_string(record, depth, key) + LINE_BREAK

    result += INTEND * depth + "}"

    return result


def render(diff_dict):
    return crawl(diff_dict)
