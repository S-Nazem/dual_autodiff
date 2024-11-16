from DualNum import Dual
import math
import pytest

def test_addition():
    """
    Test the addition of two dual numbers.
    """
    x = Dual(3,5)
    y = Dual(4,6)
    result = x + y
    assert result.real == 7
    assert result.dual == 11


def test_subtraction():
    """
    Test the subtraction of two dual numbers.
    """
    x = Dual(1,5)
    y = Dual(4,4)
    result = x - y
    assert result.real == -3
    assert result.dual == 1

def test_multiplication():
    """
    Test the multiplication of two dual numbers.
    """
    x = Dual(2,3)
    y = Dual(4,5)
    result = x * y
    assert result.real == 8
    assert result.dual == 22

def test_division():
    """
    Test the division of two dual numbers.
    """
    x = Dual(2,3)
    y = Dual(4,5)
    result = x / y
    assert result.real == 0.5
    assert result.dual == 0.125

def test_power():
    """
    Test the power of two dual numbers.
    """
    x = Dual(2,3)
    y = Dual(4,5)
    result = x ** y
    assert result.real == 16
    assert result.dual == 40

def test_division_by_zero():
    """
    Test division by zero.
    """
    a = Dual(1, 1)
    b = Dual(0, 0)
    with pytest.raises(ZeroDivisionError):
        _ = a / b

# Trigonometric and Logarithmic Functions
def test_sin():
    """
    Test the sine of a dual number.
    """
    a = Dual(math.pi / 2, 1)
    result = a.sin()
    assert pytest.approx(result.real, rel=1e-6) == 1.0  # sin(pi/2)
    assert pytest.approx(result.dual, rel=1e-6) == 0.0  # cos(pi/2)

def test_cos():
    """
    Test the cosine of a dual number.
    """
    a = Dual(0, 1)
    result = a.cos()
    assert pytest.approx(result.real, rel=1e-6) == 1.0  # cos(0)
    assert pytest.approx(result.dual, rel=1e-6) == 0.0  # -sin(0)

def test_log():
    """
    Test the natural logarithm of a dual number.
    """
    a = Dual(math.e, 1)
    result = a.log()
    assert pytest.approx(result.real, rel=1e-6) == 1.0  # log(e)
    assert pytest.approx(result.dual, rel=1e-6) == 1.0 / math.e  # 1/e

# Edge Cases and Special Values
def test_large_values():
    """
    Test the multiplication of two large dual numbers.
    """
    a = Dual(1e10, 1)
    b = Dual(2, 0.5)
    result = a * b
    assert result.real == 2e10
    assert result.dual == 0.5e10

def test_small_values():
    """
    Test the multiplication of two small dual numbers.
    """
    a = Dual(1e-10, 1)
    b = Dual(2, -0.5)
    result = a * b
    assert pytest.approx(result.real, rel=1e-6) == 2e-10
    assert pytest.approx(result.dual, rel=1e-6) == -0.5e-10

# Composite Function Test (Combination of Operations)
def test_composite_function():
    """
    Test a composite function of dual numbers.
    """
    x = Dual(2, 1)
    result = (x.sin()).log() + (x * x) * x.cos()
    assert pytest.approx(result.real, rel=1e-6) == math.log(math.sin(2)) + 4 * math.cos(2)
    assert pytest.approx(result.dual, rel=1e-6) == 2 * math.cos(2) - 4 * math.sin(2) / math.sin(2)

# Hyperbolic Functions
def test_sinh():
    """
    Test the hyperbolic sine of a dual number.
    """
    a = Dual(0, 1)
    result = a.sinh()
    assert pytest.approx(result.real, rel=1e-6) == 0.0  # sinh(0)
    assert pytest.approx(result.dual, rel=1e-6) == 1.0  # cosh(0)

def test_cosh():
    """
    Test the hyperbolic cosine of a dual number.
    """
    a = Dual(0, 1)
    result = a.cosh()
    assert pytest.approx(result.real, rel=1e-6) == 1.0  # cosh(0)
    assert pytest.approx(result.dual, rel=1e-6) == 0.0  # sinh(0)

def test_tanh():
    """
    Test the hyperbolic tangent of a dual number.
    """
    a = Dual(0, 1)
    result = a.tanh()
    assert pytest.approx(result.real, rel=1e-6) == 0.0  # tanh(0)
    assert pytest.approx(result.dual, rel=1e-6) == 1.0  # sech^2(0)

# Inverse Trigonometric Functions
def test_asin():
    """
    Test the arcsine of a dual number.
    """
    a = Dual(0.5, 1)
    result = a.asin()
    assert pytest.approx(result.real, rel=1e-6) == math.asin(0.5)
    assert pytest.approx(result.dual, rel=1e-6) == 1 / math.sqrt(1 - 0.5 ** 2)

def test_acos():
    """
    Test the arccosine of a dual number.
    """
    a = Dual(0.5, 1)
    result = a.acos()
    assert pytest.approx(result.real, rel=1e-6) == math.acos(0.5)
    assert pytest.approx(result.dual, rel=1e-6) == -1 / math.sqrt(1 - 0.5 ** 2)

def test_atan():
    """
    Test the arctangent of a dual number.
    """
    a = Dual(1, 1)
    result = a.atan()
    assert pytest.approx(result.real, rel=1e-6) == math.atan(1)
    assert pytest.approx(result.dual, rel=1e-6) == 1 / (1 + 1 ** 2)