def to_string(value):
    if value is None:
        return 'null'

    if isinstance(value, str):
        return f"'{value}'"

    if not isinstance(value, dict):
        return str(value).lower()

    return '[complex value]'


def convert_record_to_string(record, current_path):
    path = current_path.lstrip('.')
    method = record.get('action')
    result = ''
    if method == 'record_added':
        result += (
            f"Property '{path}' was added with value:"
            f" {to_string(record.get('value'))}"
        )

    if method == 'record_deleted':
        result += f"Property '{path}' was removed"

    if method == 'record_nested':
        result += render(record.get('children'), path)

    if method == 'record_changed':
        result += (
            f"Property '{path}' was updated. "
            f"From {to_string(record.get('old'))}"
            f" to {to_string(record.get('new'))}"
        )

    return result


def render(diff_dict, current_path=''):
    result = []
    for key, record in diff_dict.items():
        result.append(convert_record_to_string(
            record, f"{current_path}.{key}"))

    return '\n'.join(filter(None, result))
