from setuptools import setup, Extension
from Cython.Build import cythonize
import sysconfig
import os


python_include_dir = os.path.join(os.path.dirname(sysconfig.get_paths()["include"]), "include")


extensions = [
    Extension("DualNum_c.Dual_c", ["DualNum_c/Dual_c.pyx"], include_dirs=[python_include_dir]) 
]

setup(
    name="dual_autodiff_x",
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"}),
    packages=["DualNum_c"],
    include_package_data=False
)
