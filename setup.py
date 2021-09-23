# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rmtplot',
    version='0.1.0',
    description='A wrapper package for Plotly specialized in Random Matrices Theory(RMT) plot',
    long_description=readme,
    install_requires=['Plotly'],
    author='schifzt',
    url='https://github.com/schifzt/rmtplot-package',
    license=license,
    packages=find_packages(exclude=('tests', 'sample'))
)
