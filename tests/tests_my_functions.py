import pytest

import source.my_functions as my_functions

def test_add():
    result = my_functions.add(num1 = 1, num2 = 2)

    assert result == 3

def test_divide():
    result = my_functions.divide(num1 = 9, num2 = 3)

    assert result == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(num1 = 10, num2 = 0)