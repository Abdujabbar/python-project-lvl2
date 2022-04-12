import json
import yaml


def parse_content(content, format):
    if format == 'json':
        return json.loads(content)

    if format in ('yaml', 'yml'):
        return yaml.safe_load(content)

    raise Exception(f"Unknown format: {format}")
