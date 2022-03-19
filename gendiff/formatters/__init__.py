from .plain import render as plain_renderer
from .json import render as json_renderer
from .stylish import render as stylish_renderer


renderers_map = {
    'stylish': stylish_renderer,
    'json': json_renderer,
    'plain': plain_renderer
}
