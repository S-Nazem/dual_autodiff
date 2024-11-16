from DualNum import Dual
import math
import pytest

def test_addition():
    x = Dual(3,5)
    y = Dual(4,6)
    result = x + y
    assert result.real == 7
    assert result.dual == 11


def test_subtraction():
    x = Dual(1,5)
    y = Dual(4,4)
    result = x - y
    assert result.real == -3
    assert result.dual == 1

def test_multiplication():
    x = Dual(2,3)
    y = Dual(4,5)
    result = x * y
    assert result.real == 8
    assert result.dual == 22

def test_division():
    x = Dual(2,3)
    y = Dual(4,5)
    result = x / y
    assert result.real == 0.5
    assert result.dual == 0.125

def test_division_by_zero():
    a = Dual(1, 1)
    b = Dual(0, 0)
    with pytest.raises(ZeroDivisionError):
        _ = a / b

# Trigonometric and Logarithmic Functions
def test_sin():
    a = Dual(math.pi / 2, 1)
    result = a.sin()
    assert pytest.approx(result.real, rel=1e-6) == 1.0  # sin(pi/2)
    assert pytest.approx(result.dual, rel=1e-6) == 0.0  # cos(pi/2)

def test_cos():
    a = Dual(0, 1)
    result = a.cos()
    assert pytest.approx(result.real, rel=1e-6) == 1.0  # cos(0)
    assert pytest.approx(result.dual, rel=1e-6) == 0.0  # -sin(0)

def test_log():
    a = Dual(math.e, 1)
    result = a.log()
    assert pytest.approx(result.real, rel=1e-6) == 1.0  # log(e)
    assert pytest.approx(result.dual, rel=1e-6) == 1.0 / math.e  # 1/e

# Edge Cases and Special Values
def test_large_values():
    a = Dual(1e10, 1)
    b = Dual(2, 0.5)
    result = a * b
    assert result.real == 2e10
    assert result.dual == 0.5e10

def test_small_values():
    a = Dual(1e-10, 1)
    b = Dual(2, -0.5)
    result = a * b
    assert pytest.approx(result.real, rel=1e-6) == 2e-10
    assert pytest.approx(result.dual, rel=1e-6) == -0.5e-10

# Composite Function Test (Combination of Operations)
def test_composite_function():
    x = Dual(2, 1)
    result = (x.sin()).log() + (x * x) * x.cos()
    assert pytest.approx(result.real, rel=1e-6) == math.log(math.sin(2)) + 4 * math.cos(2)
    assert pytest.approx(result.dual, rel=1e-6) == 2 * math.cos(2) - 4 * math.sin(2) / math.sin(2)