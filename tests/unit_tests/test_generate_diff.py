from gendiff.gendiff import generate_diff
from tests import FIXTURES_PATH
def test_generate_diff_json():
    file1 = f"{FIXTURES_PATH}/json/case1/file1.json"
    file2 = f"{FIXTURES_PATH}/json/case1/file2.json"
    expected_path = f"{FIXTURES_PATH}/json/case1/expected.txt"
    
    with open(expected_path, "r") as f:
        assert "".join(f.readlines()) == generate_diff(file1, file2), "Error on result"
