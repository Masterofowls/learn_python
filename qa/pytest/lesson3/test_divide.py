import pytest
from math_utils import divide



def test_divide_zero():
    with pytest.raises(ValueError, match="cannot divide"):
        divide(10, 0)

def test_divide_ok():
    assert divide(10, 2) == 5
