from setuptools import setup, Extension
from Cython.Build import cythonize
import sysconfig
import os

# Correctly detect Python's include directory
python_include_dir = os.path.join(
    os.path.dirname(sysconfig.get_paths()["include"]), "include"
)

# Define the extension module
extensions = [
    Extension(
        "DualNum_c.Dual_c",  # Module path
        ["DualNum_c/Dual_c.pyx"],  # Source file
        include_dirs=[python_include_dir],  # Include directories
    )
]

# Setup configuration
setup(
    name="dual_autodiff_x",  # Package name
    version="0.2.0",  # Explicit version
    ext_modules=cythonize(
        extensions, compiler_directives={"language_level": "3"}
    ),
    packages=["DualNum_c"],  # List the package
    package_dir={"DualNum_c": "DualNum_c"},  # Ensure mapping is correct
    include_package_data=True,  # Include non-Python files
    zip_safe=False,  # Avoid zip-safe issues with .so files
)
