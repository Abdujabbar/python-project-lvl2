from gendiff.constants import ADDED
from gendiff.constants import CHANGED
from gendiff.constants import DELETED
from gendiff.constants import NESTED
from gendiff.constants import INTEND
from gendiff.constants import PREFIX_MAP
from gendiff.constants import LINE_BREAK
from gendiff.constants import SAME
from gendiff.renderers.json.formatter import stylish


def get_prefix(key, depth, operator):
    return f"{INTEND * depth}{PREFIX_MAP[operator]}{key}:"


def record_added(depth, key, value):
    return f"{get_prefix(key, depth, ADDED)} {stylish(value, depth + 2)}"


def record_deleted(depth, key, value):
    return f"{get_prefix(key, depth, DELETED)} {stylish(value, depth + 2)}"


def record_changed(depth, key, old_value, new_value):
    result = ""
    result += record_deleted(depth, key, old_value) + LINE_BREAK
    result += record_added(depth, key, new_value)
    return result


def record_nested(depth, key, value):
    return f"{get_prefix(key, depth, SAME)} {render(value, depth + 1)}"


def record_same(depth, key, value):
    return f"{get_prefix(key, depth, SAME)} {stylish(value, depth + 2)}"


methods = {
    ADDED: record_added,
    DELETED: record_deleted,
    CHANGED: record_changed,
    NESTED: record_nested,
    SAME: record_same,
}


def render_record(key, value, depth):
    operator, item = value

    if operator not in methods:
        raise Exception(f"Method for {operator} not implemented")

    fn = methods[operator]

    return fn(*[depth, key, *item])


def render(diff_dict, depth=0):
    result = "{\n"

    for key, value in diff_dict.items():
        result += render_record(key, value, depth) + LINE_BREAK

    result += INTEND * depth + "}" + (LINE_BREAK if depth == 0 else '')

    return result
