VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

.PHONY: test test-unittest coverage coverage-report venv install-deps activate clean

# Command to create the virtual environment
venv:
	python3 -m venv $(VENV)

# Command to install dependencies in the virtual environment
install-deps: venv
	$(PIP) install -r requirements.txt

# Command to activate the virtual environment (for informational purposes)
activate:
	source $(VENV)/bin/activate

# Command to run tests using pytest within the virtual environment
test: check-venv install-deps
	$(PYTHON) -m pytest

# Command to run tests using unittest within the virtual environment
test-unittest: check-venv install-deps
	$(PYTHON) -m unittest discover tests

# Command to run coverage tests within the virtual environment
coverage: check-venv install-deps
	$(PYTHON) -m pytest --cov=rjip tests/

# Command to generate coverage report within the virtual environment
coverage-report: coverage
	$(PYTHON) -m coverage html

# Command to clean up the virtual environment and coverage files
clean:
	rm -rf $(VENV) .coverage htmlcov

# Command to check if the virtual environment exists
check-venv:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Virtual environment not found! Creating..."; \
		$(MAKE) venv; \
	fi
