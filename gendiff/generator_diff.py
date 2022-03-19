from gendiff.parse_files import get_file_contents
from gendiff.dicts_diff import dicts_diff


def generate_diff(file1, file2):
    try:
        content1 = get_file_contents(file1)
        content2 = get_file_contents(file2)
    except Exception as e:
        print(f"Error while reading a file with an exception: {e}")
        exit(0)

    return dicts_diff(content1, content2)
