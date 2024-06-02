from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

ext_modules = [
    Extension(
        "matrix.multiply",
        ["matrix/multiply.pyx"],
    )
]

setup(
    name='matrix',
    ext_modules=cythonize(ext_modules, compiler_directives={
                          'language_level': "3"}),
)
