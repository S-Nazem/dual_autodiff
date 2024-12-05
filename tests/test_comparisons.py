import pytest
import time
from DualNum import Dual
from DualNum_c import Dual_c

def test_functional_equivalence():
    d1 = Dual(3, 2)
    d2 = Dual(4, 1)

    d1_c = Dual_c(3, 2)
    d2_c = Dual_c(4, 1)

    # Test addition
    result_dual = d1 + d2
    result_dual_c = d1_c + d2_c
    assert result_dual.real == pytest.approx(result_dual_c.real, rel=1e-6)
    assert result_dual.dual == pytest.approx(result_dual_c.dual, rel=1e-6)


def test_performance_comparison():
    # Define a function for derivative computation
    def f(x):
        return x.sin() + x.log()

    x_values = [i / 10 for i in range(1, 1000)]

    # Using Dual
    start_dual = time.time()
    derivatives_dual = [f(Dual(x, 1)).dual for x in x_values]
    end_dual = time.time()

    # Using Dual_c
    start_dual_c = time.time()
    derivatives_dual_c = [f(Dual_c(x, 1)).dual for x in x_values]
    end_dual_c = time.time()

    # Ensure results are equivalent
    for d_dual, d_dual_c in zip(derivatives_dual, derivatives_dual_c):
        assert pytest.approx(d_dual, 1e-6) == pytest.approx(d_dual_c, 1e-6)

    # Compare performance
    time_dual = end_dual - start_dual
    time_dual_c = end_dual_c - start_dual_c

    print(f"Time using Dual: {time_dual:.4f}s")
    print(f"Time using Dual_c: {time_dual_c:.4f}s")
    print(f"Speedup: {100 * (time_dual - time_dual_c) / time_dual:.2f}%")
    assert time_dual_c < time_dual  # Ensure Dual_c is faster

def test_stress_test():
    # Large range for derivative computation
    def f(x):
        return x.exp() + x.sqrt()

    # Restrict x_values to avoid overflow in exp
    x_values = [i / 10 for i in range(1, 500)]  # Adjust the range to avoid overflow

    # Using Dual
    derivatives_dual = [f(Dual(x, 1)).dual for x in x_values]

    # Using Dual_c
    derivatives_dual_c = [f(Dual_c(x, 1)).dual for x in x_values]

    # Compare derivatives
    assert all(pytest.approx(d1, rel=1e-6) == d2 for d1, d2 in zip(derivatives_dual, derivatives_dual_c))

