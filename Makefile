.PHONY: test

test:
	pytest

# Same as 'test' command, but using unittest package
test-unittest:
	python3 -m unittest discover tests

coverage:
	pytest --cov=rji_cli tests/ 

coverage-report:
	coverage html