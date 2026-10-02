import pytest
from math_utils import divide

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (0, 5, 0),
        (-4, 2, -2),
    ],
)
def test_divide_many(a, b, expected):
    assert divide(a, b) == expected

@pytest.mark.parametrize("b", [0])
def test_divide_zero(b):
    with pytest.raises(ValueError):
        divide(1, b)