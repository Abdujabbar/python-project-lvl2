def render_value(value):
    if value is None:
        return 'null'

    if isinstance(value, str):
        return f"'{value}'"

    if not isinstance(value, dict):
        return str(value).lower()

    return '[complex value]'


def record_added(current_path, value):
    path = current_path.lstrip('.')
    return (
        f"Property '{path}' was added with value: {render_value(value)}"
    )


def record_deleted(current_path, value):
    return f"Property '{current_path.lstrip('.')}' was removed"


def record_changed(current_path, old_value, new_value):
    path = current_path.lstrip('.')
    old_value = render_value(old_value)
    new_value = render_value(new_value)

    return f"Property '{path}' was updated. From {old_value} to {new_value}"


def record_nested(current_path, value):
    return render(value, current_path)


def record_same(current_path, value):
    return ''


def render(diff_dict, current_path=''):
    result = []
    for key, value in diff_dict.items():
        method = value.get('method')
        item = value.get('item')
        current_record = globals()[method](*[f"{current_path}.{key}", *item])
        result.append(current_record)

    return '\n'.join(filter(None, result))
