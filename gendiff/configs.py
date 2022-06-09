from gendiff.dicts import build_diff
from gendiff.formatters import formatter
from gendiff.parser import parse_content


def get_content(path):
    with open(path, "r") as file_content:
        return parse_content(file_content.read(), path.split(".")[-1])


def generate_diff(file1, file2, format='stylish'):

    content1 = get_content(file1)
    content2 = get_content(file2)

    diff = build_diff(content1, content2)

    return formatter(format, diff)
