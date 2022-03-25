from .plain import render as plain_renderer
from .json import render as json_renderer
from .stylish import render as stylish_renderer


def get_renderer(format):
    renderers_map = {
        'stylish': stylish_renderer,
        'json': json_renderer,
        'plain': plain_renderer
    }

    if format not in renderers_map.keys() or not renderers_map[format]:
        raise Exception(f"Not implemented method for format: {format}")

    return renderers_map[format]
