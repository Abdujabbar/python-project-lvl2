from .plain import render as plain_renderer
from .json import render as json_renderer
from .stylish import render as render_stylish


def formatter(format, dicts_diff):
    renderers_map = {
        'stylish': render_stylish,
        'json': json_renderer,
        'plain': plain_renderer
    }

    if format not in renderers_map.keys() or not renderers_map[format]:
        raise Exception(f"Not implemented method for format: {format}")

    return renderers_map[format](dicts_diff)
