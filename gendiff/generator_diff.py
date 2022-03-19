from gendiff.parse_files import get_file_contents
from gendiff.dicts_diff import dicts_diff
from gendiff.formatters import renderers_map


def generate_diff(file1, file2, format):

    if format not in renderers_map.keys() or not renderers_map[format]:
        raise Exception(f"Not implemented method for format: {format}")

    renderer = renderers_map[format]

    try:
        content1 = get_file_contents(file1)
        content2 = get_file_contents(file2)
    except Exception as e:
        print(f"Error while reading a file with an exception: {e}")
        exit(0)

    return renderer(dicts_diff(content1, content2))
