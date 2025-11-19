import pytest
from calculator.core import add, sub, mul, div, operate

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3

def test_mul():
    assert mul(4, 3) == 12

def test_div():
    assert div(10, 2) == 5

def test_div_zero():
    with pytest.raises(ValueError):
        div(1, 0)

@pytest.mark.parametrize("op,a,b,expected", [
    ("add", 1, 2, 3),
    ("sub", 5, 3, 2),
    ("mul", 2, 4, 8),
    ("div", 8, 2, 4),
])
def test_operate(op, a, b, expected):
    assert operate(a, b, op) == expected

def test_operate_invalid():
    with pytest.raises(ValueError):
        operate(1, 2, "pow")
