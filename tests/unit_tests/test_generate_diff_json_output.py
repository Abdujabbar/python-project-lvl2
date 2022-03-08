from gendiff.gendiff import generate_diff
from gendiff.renderers.json.render import render as json_renderer
from tests import FIXTURES_PATH


def test_generate_diff_as_json_output_for_json_files():
    file1 = f"{FIXTURES_PATH}/json/case1/file1.json"
    file2 = f"{FIXTURES_PATH}/json/case1/file2.json"
    expected_path = f"{FIXTURES_PATH}/json/case1/expected_json.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, json_renderer), f"Error on result, result"


def test_generate_diff_as_json_output_for_yaml_files():
    file1 = f"{FIXTURES_PATH}/yaml/case1/file1.yml"
    file2 = f"{FIXTURES_PATH}/yaml/case1/file2.yml"
    expected_path = f"{FIXTURES_PATH}/yaml/case1/expected_json.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, json_renderer), "Error on result"


def test_generate_diff_as_nested_json_output_for_json_files():
    file1 = f"{FIXTURES_PATH}/json/case2/file1.json"
    file2 = f"{FIXTURES_PATH}/json/case2/file2.json"
    expected_path = f"{FIXTURES_PATH}/json/case2/expected_json.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, json_renderer), f"Error on result, result"


def test_generate_diff_as_nested_json_output_for_yaml_files():
    file1 = f"{FIXTURES_PATH}/yaml/case2/file1.yml"
    file2 = f"{FIXTURES_PATH}/yaml/case2/file2.yml"
    expected_path = f"{FIXTURES_PATH}/yaml/case2/expected_json.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, json_renderer), "Error on result"
