#!/bin/bash

# Install a package locally
python setup.py bdist_wheel
pip install dist/rmtplot-0.1.0-py3-none-any.whl
