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

checktypes:  ## check types with mypy
	mypy --ignore-missing-imports manly_randomization_test

checkstyle:  ## check style with flake8 and black
	## Ignore flake8 F401, F403 and F405 errors as we want to be able to use star (*) imports
	## Ignore flake8 F811, 821 and W503 errors as enforcement changed between python 3.7 and 3.8
	flake8 --ignore F401,F403,F405,F811,F821,W503 --max-complexity 10 manly_randomization_test tests
	isort --check-only --profile black manly_randomization_test tests
	black --check --diff manly_randomization_test tests