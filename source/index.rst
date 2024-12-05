.. dual_autodiff documentation master file, created by
   sphinx-quickstart on Tue Nov 14 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root toctree directive.

Welcome to DualNum's Documentation
===================================

DualNum is a Python package designed for automatic differentiation using dual numbers. It provides an intuitive interface for operations like computing derivatives and supports common mathematical functions.

**Features**:
- Perform arithmetic operations with dual numbers.
- Compute derivatives of complex functions effortlessly.
- Extensive support for transcendental functions (e.g., sin, cos, log).
- Includes a Cythonized version (`Dual_c`) for improved performance.

Get started quickly by following our `Quickstart Guide <#quick-example>`_.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   cythonized

Installation
============

Install DualNum using pip:

.. code-block:: bash

    pip install dual_autodiff

Alternatively, clone the repository and install it locally:

.. code-block:: bash

    git clone https://gitlab.developers.cam.ac.uk/phy/data-intensive-science-mphil/assessments/c1_coursework1/sn665/-/tree/dev?ref_type=heads
    cd dual_autodiff
      pip install -e .
    cd dual_autodiff_x
      pip install -e .

Quick Example
=============

Here's a quick example of how to use the `Dual` class in the `DualNum` module:

.. code-block:: python

    from DualNum import Dual

    # Create a dual number with real part 2 and dual part 1
    x = Dual(2, 1)

    # Perform some operations
    y = x + x
    z = x.sin() + x.log()

    print("y:", y)
    print("z:", z)


Computing Derivatives (Automatic Differentiation)
=================================================

Use the `compute_derivative` function to compute derivatives of functions at specific points using dual numbers.

Example:

.. code-block:: python

    from DualNum import compute_derivative, Dual

    def func(x):
        return (x.sin()).log() + (x * x * x.cos())

    x = 1.5
    derivative = compute_derivative(func, x, Dual)
    print(f"The derivative at x={x} is {derivative}")

For the Cythonized version:

.. code-block:: python

    from DualNum_c import compute_derivative, Dual_c

    def func(x):
        return (x.sin()).log() + (x * x * x.cos())

    x = 1.5
    derivative = compute_derivative(func, x, Dual_c)
    print(f"The derivative at x={x} is {derivative}")



Visualization Example
=====================

Here's an example of computing and visualizing a derivative with DualNum:

.. plot::

   import matplotlib.pyplot as plt
   from DualNum import Dual

   def f(x):
       return (x.sin()).log() + ((x * x) * x.cos())

   # Filter out invalid x values (where sin(x) <= 0)
   x = [i / 10 for i in range(1, 100) if Dual(i / 10, 1).sin().real > 0]
   y = [f(Dual(i, 1)).dual for i in x]

   plt.plot(x, y, label='Derivative')
   plt.legend()
   plt.xlabel("x")
   plt.ylabel("f'(x)")
   plt.title("Derivative Visualization")
   plt.show()


DualNum and Dual_c
==================

`DualNum` includes two implementations of dual numbers:
1. **`Dual`**: A pure Python implementation, ideal for debugging and prototyping.
2. **`Dual_c`**: A Cythonized implementation that provides the same functionality as `Dual`, but is optimized for performance.

When to use:
- Use `Dual` for flexibility and ease of debugging.
- Use `Dual_c` for computationally intensive tasks where performance is critical.

Example usage of `Dual_c`:

.. code-block:: python

    from DualNum_c import Dual_c

    # Create a dual number with real part 3 and dual part 1
    x = Dual_c(3, 1)

    # Perform some operations
    y = x + x
    z = x.sin() + x.log()

    print("y:", y)
    print("z:", z)

Use `Dual_c` in the same way as `Dual`, as their APIs are identical.



Notebooks
=========
Explore the following notebooks for practical use cases:

.. toctree::
   :maxdepth: 1
   :caption: Notebooks

   notebooks/tutorial
   notebooks/dual_autodiff



Acknowledgments
===============

This project was developed as part of a coursework on data-intensive science. Special thanks to Boris for the continued help on the discord/lectures throughout the term.
