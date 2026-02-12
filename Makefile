.PHONY: install lint format test coverage ci

install:
	pip install -e .[dev]


format:
	isort .
	black .

test:
	pytest -q

coverage:
	pytest --cov=src/buergerregister --cov-branch --cov-report=html

ci:
	make test
	make coverage
