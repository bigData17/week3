from distutils.core import setup
from Cython.Build import cythonize
setup(name = "Cython Version", ext_modules = cythonize('sumcython.pyx'), )