import pytest
from gendiff import generate_diff

from tests import FIXTURES_PATH


@pytest.mark.parametrize("file1, file2, expected_path, format", [
    (
        f"{FIXTURES_PATH}/file1.json",
        f"{FIXTURES_PATH}/file2.json",
        f"{FIXTURES_PATH}/result_stylish",
        "stylish"
    ),
   (
        f"{FIXTURES_PATH}/file1.json",
        f"{FIXTURES_PATH}/file2.json",
        f"{FIXTURES_PATH}/result_plain",
        "plain"
    ),
    (
        f"{FIXTURES_PATH}/file1.yml",
        f"{FIXTURES_PATH}/file2.yml",
        f"{FIXTURES_PATH}/result_stylish",
        "stylish"
    ),
   (
        f"{FIXTURES_PATH}/file1.yml",
        f"{FIXTURES_PATH}/file2.yml",
        f"{FIXTURES_PATH}/result_plain",
        "plain"
    ),
])
def test_gen_diff_output(file1, file2, expected_path, format):
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2, format), f"Error on result, result"
