Cythonized Version: DualNum_c
=============================

DualNum_c is the Cythonized version of the `DualNum` module. It provides the same API but is optimized for performance, making it ideal for scenarios where computational efficiency is critical.

**Features**:
- **Significant Speedup**: Optimized computations for performance-critical tasks.
- **Identical API**: Seamlessly interchangeable with `DualNum`.
- **Ideal for Large Workloads**: Best suited for tasks requiring repetitive or large-scale automatic differentiation.


Example Usage
-------------
Using `Dual_c` is straightforward and mirrors the `Dual` class. Below is a simple example:

.. code-block:: python

    from DualNum_c import Dual_c

    x = Dual_c(3, 1)
    y = x.sin() + x.log()
    print("y:", y)

**When to Use Dual_c**:
- Use `Dual_c` for high-performance tasks or large-scale computations.
- Use `Dual` for debugging, as the Python implementation provides better error tracebacks and is easier to debug.

**Note**:
The `Dual_c` class sacrifices some debugging flexibility in favor of speed. For development, you may prefer using `Dual` and switch to `Dual_c` for production or performance-critical use cases.



Performance Comparison
----------------------
To demonstrate the performance improvement, consider the following task: computing the derivative of a mathematical function at multiple points.

**Benchmark Task**: Compute the derivative of `f(x) = log(sin(x)) + x^2 * cos(x)` at 10,000 evenly spaced points in the range `[1, 100]`.

.. code-block:: python

   import time
   import numpy as np
   from DualNum import Dual
   from DualNum_c import Dual_c

   def f(x):
      return x.exp() * x.cos() * x.sin()

   # Define the range and points
   x_values = np.linspace(1, 100, 10000)

   # Using Dual (Python version)
   start_python = time.time()
   derivatives_python = [f(Dual(x, 1)).dual for x in x_values]
   end_python = time.time()
   time_python = end_python - start_python

   # Using Dual_c (Cython version)
   start_cython = time.time()
   derivatives_cython = [f(Dual_c(x, 1)).dual for x in x_values]
   end_cython = time.time()
   time_cython = end_cython - start_cython

   # Compare the performance
   speedup = (time_python - time_cython) / time_python * 100
   print(f"Python Version Time: {time_python:.4f} seconds")
   print(f"Cython Version Time: {time_cython:.4f} seconds")
   print(f"Speedup: {speedup:.2f}%")


The results highlight the computational efficiency of the Cythonized version.

**Sample Output**:

Python Version Time: 0.0421 seconds
Cython Version Time: 0.0335 seconds
Speedup: 20.32%



