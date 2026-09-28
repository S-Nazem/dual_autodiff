# DualNum Package

The **DualNum** package is a Python library for automatic differentiation using dual numbers. It enables precise computation of derivatives and supports a wide range of mathematical operations via the class **Dual**. Additionally, the package includes a Cythonized version, **Dual_c**, for improved performance in computationally intensive tasks.

---

## Features
- **Automatic Differentiation**: Compute derivatives of complex functions with ease.
- **Wide Mathematical Support**: Includes common operations like `sin`, `cos`, `log`, `exp`, and more.
- **Custom Derivative Computation**: Use the `compute_derivative` function to compute derivatives at specific points.
- **Cythonized Version**: Leverage the **Dual_c** module for faster computations while maintaining the same API.
- **Robust Error Handling**: Safeguards against invalid mathematical operations (e.g., log of non-positive numbers).
- **Integration with Scientific Tools**: Compatible with Python scientific libraries like NumPy and Matplotlib for advanced visualization and computation.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/S-Nazem/dual_autodiff.git
   cd dual_autodiff
   ```

2. Create an environment and install the Python package (Python 3.9+):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -e .
   ```

3. Optional: Build the Cython version (requires a C compiler):
   ```bash
   python -m pip install -e ./dual_autodiff_x
   ```

---

## Pre-built wheels 

Pre-built Cython wheels are available in `dist_wheels` for Linux x86-64 with CPython 3.10 or 3.11. Choose the wheel matching your interpreter; these are alternatives to building the Cython extension from source. Install the Python package above separately.

### Installation

For CPython 3.10:

```bash
pip install dist_wheels/dual_autodiff_x-0.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```
For CPython 3.11:

```bash
pip install dist_wheels/dual_autodiff_x-0.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```
Import after installing the Python package and a matching Cython wheel:

```python
from DualNum import Dual, compute_derivative
from DualNum_c import Dual_c
```

---

## Usage

Here's a quick example on how to use the **Dual** class:

```python
from DualNum import Dual, compute_derivative

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

To use the Dual_c class (Cythonized version):

```python
from DualNum_c import Dual_c

# Create a dual number with real part 2 and dual part 1
x = Dual_c(2, 1)

# Perform operations
y = x.sin() + x.log()
print("Result:", y)
```
---

## Documentation

From the repository root, install the documentation dependencies and build the HTML pages:

```bash
python -m pip install sphinx sphinx-rtd-theme nbsphinx matplotlib
make html
```

Open `build/html/index.html` in your browser. Rendering notebook documentation may also require Pandoc. The full `requirements.txt` is a historical development-environment snapshot and includes editable references to an older commit; it is not required for the basic Python installation.

---

## Source

[GitHub repository](https://github.com/S-Nazem/dual_autodiff)

---

## License

The package metadata declares the MIT License. A standalone license file is not currently included in the repository.

