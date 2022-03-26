def render_node(value):
    if value is None:
        return 'null'

    if isinstance(value, str):
        return f"'{value}'"

    if not isinstance(value, dict):
        return str(value).lower()

    return '[complex value]'


def render_record(current_path, record):
    path = current_path.lstrip('.')
    method = record.get('action')
    result = ''
    if method == 'record_added':
        result += (
            f"Property '{path}' was added with value:"
            f" {render_node(record.get('node'))}"
        )

    if method == 'record_deleted':
        result += f"Property '{path}' was removed"

    if method == 'record_nested':
        result += render_helper(record.get('children'), path)

    if method == 'record_changed':
        result += (
            f"Property '{path}' was updated. "
            f"From {render_node(record.get('old'))}"
            f" to {render_node(record.get('new'))}"
        )

    return result


def render_helper(diff_dict, current_path=''):
    result = []
    for key, record in diff_dict.items():
        current_record = render_record(f"{current_path}.{key}", record)
        result.append(current_record)

    return '\n'.join(filter(None, result))


def render(diff_dict):
    return render_helper(diff_dict)
