from gendiff.renderers.plain.formatter import stylish
from gendiff.constants import ADDED, CHANGED, DELETED, NESTED, SAME


def record_added(current_path, value):
    path = current_path.lstrip('.')
    return (
        f"Property '{path}' was added with value: {stylish(value)}"
    )


def record_deleted(current_path, value):
    return f"Property '{current_path.lstrip('.')}' was removed"


def record_changed(current_path, old_value, new_value):
    path = current_path.lstrip('.')
    old_value = stylish(old_value)
    new_value = stylish(new_value)

    return f"Property '{path}' was updated. From {old_value} to {new_value}"


def record_nested(current_path, value):
    return render(value, current_path)


def record_same(current_path, value):
    return ''


methods = {
    ADDED: record_added,
    DELETED: record_deleted,
    CHANGED: record_changed,
    NESTED: record_nested,
    SAME: record_same
}


def render_record(current_path, value):
    operator, item = value

    if operator not in methods:
        raise Exception(f"Method for {operator} not implemented")

    fn = methods[operator]

    return fn(*[current_path, *item])


def render(diff_dict, current_path=''):
    result = []
    for k, v in diff_dict.items():
        current_record = render_record(f"{current_path}.{k}", v)
        result.append(current_record)

    return '\n'.join(filter(None, result))
