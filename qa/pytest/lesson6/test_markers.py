import pytest 
from math_utils import divide

def test_divide_ok():
    assert divide(10, 2) == 5

@pytest.mark.skip(reason="not implemented yet")
def test_not_ready():
    assert divide(2,2) == 1

@pytest.mark.xfail(reason="known bug")
def test_known_bug():
    assert divide(1, 0) == 'error'

@pytest.mark.slow
def test_slow_thing():
    assert divide(1000, 2) == 500