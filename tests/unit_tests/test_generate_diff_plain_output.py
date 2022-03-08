from gendiff.gendiff import generate_diff
from gendiff.renderers.plain.render import render as plain_renderer
from tests import FIXTURES_PATH


def test_generate_diff_as_plain_output_for_json_files():
    file1 = f"{FIXTURES_PATH}/json/case1/file1.json"
    file2 = f"{FIXTURES_PATH}/json/case1/file2.json"
    expected_path = f"{FIXTURES_PATH}/json/case1/expected_plain.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, plain_renderer), f"Error on result, result"


def test_generate_diff_as_plain_output_for_yaml_files():
    file1 = f"{FIXTURES_PATH}/yaml/case1/file1.yml"
    file2 = f"{FIXTURES_PATH}/yaml/case1/file2.yml"
    expected_path = f"{FIXTURES_PATH}/yaml/case1/expected_plain.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, plain_renderer), "Error on result"


def test_generate_diff_as_nested_plain_output_for_json_files():
    file1 = f"{FIXTURES_PATH}/json/case2/file1.json"
    file2 = f"{FIXTURES_PATH}/json/case2/file2.json"
    expected_path = f"{FIXTURES_PATH}/json/case2/expected_plain.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, plain_renderer), f"Error on result, result"


def test_generate_diff_as_nested_plain_output_for_yaml_files():
    file1 = f"{FIXTURES_PATH}/yaml/case2/file1.yml"
    file2 = f"{FIXTURES_PATH}/yaml/case2/file2.yml"
    expected_path = f"{FIXTURES_PATH}/yaml/case2/expected_plain.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, plain_renderer), "Error on result"
