from gendiff.dicts import build_difference
from gendiff.formatters import formatter
from gendiff.files import parse_content


def generate_diff(file1, file2, format='stylish'):

    content1 = parse_content(file1)
    content2 = parse_content(file2)

    diff = build_difference(content1, content2)

    return formatter(format, diff)
