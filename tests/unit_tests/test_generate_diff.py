from gendiff.gendiff import generate_diff
from gendiff.renderers.json.json import render as render_json
from tests import FIXTURES_PATH


def test_generate_diff_json():
    file1 = f"{FIXTURES_PATH}/json/case1/file1.json"
    file2 = f"{FIXTURES_PATH}/json/case1/file2.json"
    expected_path = f"{FIXTURES_PATH}/json/case1/expected.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, render_json), f"Error on result, result"


def test_generate_diff_yaml():
    file1 = f"{FIXTURES_PATH}/yaml/case1/file1.yml"
    file2 = f"{FIXTURES_PATH}/yaml/case1/file2.yml"
    expected_path = f"{FIXTURES_PATH}/yaml/case1/expected.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, render_json), "Error on result"


def test_generate_diff_nested_json():
    file1 = f"{FIXTURES_PATH}/json/case2/file1.json"
    file2 = f"{FIXTURES_PATH}/json/case2/file2.json"
    expected_path = f"{FIXTURES_PATH}/json/case2/expected.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, render_json), f"Error on result, result"


def test_generate_diff_nested_yaml():
    file1 = f"{FIXTURES_PATH}/yaml/case2/file1.yml"
    file2 = f"{FIXTURES_PATH}/yaml/case2/file2.yml"
    expected_path = f"{FIXTURES_PATH}/yaml/case2/expected.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, render_json), "Error on result"
