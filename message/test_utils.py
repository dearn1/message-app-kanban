# test_utils_pytest.py

import pytest
from .utils import add, subtract, multiply, divide

def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5

def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(1, 3) == pytest.approx(0.3333333333333333) # Use pytest.approx for floats

    # Test that dividing by zero raises a ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
