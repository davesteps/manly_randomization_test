.PHONY: install-dev test lint

install-dev:
	pip install -e .[dev]

test:
	pytest

lint:
	flake8

fixstyle:  ## fix black and isort style violations
	isort --profile black manly_randomization_test tests
	black manly_randomization_test tests