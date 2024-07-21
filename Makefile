VENV := venv
PYTHON := $(VENV)/bin/python

PHONY: test test-unittest coverage coverage-report venv install-deps clean

venv:
	python3 -m venv $(VENV)
	@echo "\nRun 'source $(VENV)/bin/activate' to start virtual environment"

install-deps:
	pip install -r requirements-dev.txt

test:
	pytest

# Same as 'test' command, but using unittest package
test-unittest:
	python3 -m unittest discover tests

coverage:
	pytest --cov=rjip tests/ 

coverage-report:
	coverage html

clean:
	rm -rf $(VENV) .coverage htmlcov