.PHONY: test

test:
	pytest

coverage:
	pytest --cov=rji_cli tests/ 

coverage-report:
	coverage html

test-unittest:
	python3 -m unittest discover tests