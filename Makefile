.PHONY: install-dev test lint

install-dev:
	pip install -e .[dev]

test:
	pytest

lint:
	flake8

format:
	black .
