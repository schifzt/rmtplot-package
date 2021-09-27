install:
	python setup.py bdist_wheel
# pip install dist/rmtplot-0.1.0-py3-none-any.whl
	pip install -e ${PWD}

# test:
	# nosetests tests
