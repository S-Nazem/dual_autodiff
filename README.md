# DualNum Package

The **DualNum**  package is a Python library for automatic differentiation using dual numbers. It enables precise computation of derivatives and supports a wide range of mathematical operations via the class **Dual**. Additionally, the package includes a Cythonized version, **Dual_c**, for improved performance in computationally intensive tasks.

## Features
- **Automatic Differentiation**: Compute derivatives of complex functions with ease.
- **Wide Mathematical Support**: Includes common operations like `sin`, `cos`, `log`, `exp`, and more.
- **Custom Derivative Computation**: Use the `compute_derivative` function to compute derivatives at specific points.
- **Cythonized Version**: Leverage the **Dual_c** module for faster computations while maintaining the same API.
- **Robust Error Handling**: Safeguards against invalid mathematical operations (e.g., log of non-positive numbers).
- **Integration with Scientific Tools**: Compatible with Python scientific libraries like NumPy and Matplotlib for advanced visualization and computation.

## Installation

1. Clone this repository:
   ```bash
   git clone https://gitlab.com/yourusername/dual_autodiff.git
   cd dual_autodiff
   ```

2. Install the DualNum (python) package and the dependancies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

3. Optional: Install the cythonized version
   ```bash
   cd dual_autodiff_x
   pip install -e .
   ```

## Usage

Here's a quick example on how to use the **Dual** class:

    ```python
    from DualNum import Dual

    # Create a dual number with real part 2 and dual part 1
    x = Dual(2, 1)

    # Perform operations
    y = x.sin() + x.log()
    print("Result:", y)

    # Compute a derivative
    def f(x):
        return x.sin() + x.log()

    derivative = compute_derivative(f, 2, Dual)
    print("Derivative at x=2:", derivative)
    ```

## Documentation

To view the documentation locally:

1. Ensure you have Sphinx installed:
   ```bash
   pip install -r requirements.txt

2. Navigate to the source
    ```bash
    cd dual_autodiff

3. Build and open the documentation
    ```bash
    make html
    open build/html/index.html
    ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

