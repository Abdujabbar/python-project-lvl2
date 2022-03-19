import pytest
from gendiff.formatters import renderers_map
from gendiff.generator_diff import generate_diff
from tests import FIXTURES_PATH


@pytest.mark.parametrize("file1, file2, expected_path, format", [
    (
        f"{FIXTURES_PATH}/json/case1/file1.json",
        f"{FIXTURES_PATH}/json/case1/file2.json",
        f"{FIXTURES_PATH}/json/case1/expected_stylish.txt",
        "stylish"
    ),
    (
        f"{FIXTURES_PATH}/json/case2/file1.json",
        f"{FIXTURES_PATH}/json/case2/file2.json",
        f"{FIXTURES_PATH}/json/case2/expected_stylish.txt",
        "stylish"
    ),
    (
        f"{FIXTURES_PATH}/yaml/case1/file1.yml",
        f"{FIXTURES_PATH}/yaml/case1/file2.yml",
        f"{FIXTURES_PATH}/yaml/case1/expected_plain.txt",
        "plain"
    ),
    (
        f"{FIXTURES_PATH}/yaml/case2/file1.yml",
        f"{FIXTURES_PATH}/yaml/case2/file2.yml",
        f"{FIXTURES_PATH}/yaml/case2/expected_plain.txt",
        "plain"
    )
])
def test_gen_diff_output(file1, file2, expected_path, format):
    with open(expected_path, "r") as f:
        dicts_diff = generate_diff(file1, file2)
        renderer = renderers_map[format]
        assert "".join(f.readlines()) == renderer(dicts_diff), f"Error on result, result"
