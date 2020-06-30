.PHONY: venv install test-install test test-integ clean nopyc

venv: clean
	@python --version || (echo "Python is not installed, please install Python 3"; exit 1);
	virtualenv --python=python venv

install: venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; pip install -r install-requirements.pip

test-install: install
	. venv/bin/activate; pip install -r test-requirements.pip

test: test-install

test-integ: test
	. venv/bin/activate; coverage run -m unittest discover

clean: nopyc
	rm -rf venv

nopyc:
	find . -name \*.pyc -delete
