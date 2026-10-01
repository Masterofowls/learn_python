from math_utils import double

def test_double_positive():
    # Arrange
    n = 4
    # Act
    result = double(n)
    # Assert
    assert result == 8

def test_double_zero():
    n = 0
    result = double(n)
    assert result == 0

def test_double_negative():
    n = -1
    result = double(n)
    assert result == -2
