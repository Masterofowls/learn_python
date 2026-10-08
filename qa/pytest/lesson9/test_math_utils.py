from math_utils import divide, double
import pytest

def test_divide_zero():
    with pytest.raises(ValueError, match="cannot divide"):
        divide(10, 0)

def test_divide_ok():
    assert divide(10, 2) == 5

def test_double():
    assert double(5, 2) == 10