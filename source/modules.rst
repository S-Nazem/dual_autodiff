DualNum module
==============

.. automodule:: DualNum
   :members:
   :undoc-members:
   :show-inheritance:

The `DualNum` module provides the `Dual` class for dual number arithmetic and automatic differentiation. It allows users to perform mathematical operations on dual numbers, including addition, subtraction, multiplication, division, exponentiation, trigonometric functions, and logarithmic functions.

Example Usage
-------------
Here's a quick example of how to use the `Dual` class from the `DualNum` module:

.. code-block:: python

    from DualNum import Dual

    # Create a dual number with real part 2 and dual part 1
    x = Dual(2, 1)

    # Perform some operations
    y = x + x
    z = x.sin() + x.log()

    print("y:", y)
    print("z:", z)
