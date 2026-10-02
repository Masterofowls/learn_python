import pytest
from math_utils import divide

@pytest.fixture
def sample_numbers():
    return {"a": 10, "b": 2}

def test_divide_with_fixture(sample_numbers):
    result = divide(sample_numbers["a"], sample_numbers["b"])
    assert result == 5

@pytest.fixture
def temp_note(tmp_path):
    path = tmp_path / "note.txt"
    path.write_text("4", encoding="utf-8")
    yield path

def test_divide_from_file(temp_note):
    text = temp_note.read_text(encoding="utf-8")
    assert divide(int(text), 2) == 2