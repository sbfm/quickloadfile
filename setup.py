# coding: utf-8
from setuptools import setup, find_packages
from glob import glob

setup(
    name="quickloadvalue",
    version="0.1.0",
    license='MIT',
    description="quick load value",

    author="Fumiya-Shibamata",
    url="https://github.com/sbfm/ConfigController",

    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
)
