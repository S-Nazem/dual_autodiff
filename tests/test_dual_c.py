import pytest
from DualNum import Dual, compute_derivative
from DualNum_c import Dual_c as Dual
import math

def test_init():
    # Test initialization with valid inputs
    d = Dual(2.0, 3.0)
    assert d.real == 2.0
    assert d.dual == 3.0

    # Test initialization with invalid inputs
    with pytest.raises(TypeError):
        Dual("2.0", 3.0)
    with pytest.raises(TypeError):
        Dual(2.0, "3.0")

def test_addition():
    d1 = Dual(2, 1)
    d2 = Dual(3, 4)
    result = d1 + d2
    assert result.real == 5
    assert result.dual == 5

    with pytest.raises(TypeError):
        d1 + 5

def test_subtraction():
    d1 = Dual(5, 3)
    d2 = Dual(2, 1)
    result = d1 - d2
    assert result.real == 3
    assert result.dual == 2

    with pytest.raises(TypeError):
        d1 - 5

def test_multiplication():
    d1 = Dual(2, 3)
    d2 = Dual(4, 5)
    result = d1 * d2
    assert result.real == 8
    assert result.dual == 22

    with pytest.raises(TypeError):
        d1 * 5

def test_division():
    d1 = Dual(10, 4)
    d2 = Dual(2, 1)
    result = d1 / d2
    assert result.real == 5
    assert pytest.approx(result.dual, 1e-6) == -0.5

    with pytest.raises(TypeError):
        d1 / 5

    with pytest.raises(ZeroDivisionError):
        d1 / Dual(0, 0)

def test_power():
    d1 = Dual(2, 3)
    d2 = Dual(3, 4)
    result = d1 ** d2
    assert pytest.approx(result.real, 1e-6) == 8
    assert pytest.approx(result.dual, 1e-6) == 58.18070977791825

    with pytest.raises(TypeError):
        d1 ** 5

def test_equality():
    d1 = Dual(2, 3)
    d2 = Dual(2, 3)
    d3 = Dual(3, 2)
    assert d1 == d2
    assert d1 != d3

def test_sin():
    d = Dual(math.pi / 2, 1)
    result = d.sin()
    assert pytest.approx(result.real, 1e-6) == 1
    assert pytest.approx(result.dual, 1e-6) == 0

def test_cos():
    d = Dual(0, 1)
    result = d.cos()
    assert pytest.approx(result.real, 1e-6) == 1
    assert pytest.approx(result.dual, 1e-6) == 0

def test_tan():
    d = Dual(math.pi / 4, 1)
    result = d.tan()
    assert pytest.approx(result.real, 1e-6) == 1
    assert pytest.approx(result.dual, 1e-6) == 2

def test_exp():
    d = Dual(1, 1)
    result = d.exp()
    assert pytest.approx(result.real, 1e-6) == math.exp(1)
    assert pytest.approx(result.dual, 1e-6) == math.exp(1)

def test_log():
    d = Dual(math.e, 1)
    result = d.log()
    assert pytest.approx(result.real, 1e-6) == 1
    assert pytest.approx(result.dual, 1e-6) == 1 / math.e

    with pytest.raises(ValueError):
        Dual(0, 1).log()

def test_sqrt():
    d = Dual(4, 1)
    result = d.sqrt()
    assert pytest.approx(result.real, 1e-6) == 2
    assert pytest.approx(result.dual, 1e-6) == 0.25

def test_hyperbolic():
    d = Dual(0, 1)
    assert pytest.approx(d.sinh().real, 1e-6) == 0
    assert pytest.approx(d.sinh().dual, 1e-6) == 1

    assert pytest.approx(d.cosh().real, 1e-6) == 1
    assert pytest.approx(d.cosh().dual, 1e-6) == 0

    assert pytest.approx(d.tanh().real, 1e-6) == 0
    assert pytest.approx(d.tanh().dual, 1e-6) == 1

def test_trigonometric_inverse():
    d = Dual(0.5, 1)
    assert pytest.approx(d.asin().real, 1e-6) == math.asin(0.5)
    assert pytest.approx(d.asin().dual, 1e-6) == 1.1547

    assert pytest.approx(d.acos().real, 1e-6) == math.acos(0.5)
    assert pytest.approx(d.acos().dual, 1e-6) == -1.1547

    assert pytest.approx(d.atan().real, 1e-6) == math.atan(0.5)
    assert pytest.approx(d.atan().dual, 1e-6) == 0.8

def test_compute_derivative():
    def f(x):
        return x.sin() + x.log()

    x = 1.5
    derivative = compute_derivative(f, x, Dual)
    assert pytest.approx(derivative, 1e-6) == math.cos(1.5) + 1 / 1.5
