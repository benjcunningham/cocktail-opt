.PHONY: install quality style

check_dirs := src setup.py tests

install:
	pip install -e ".[dev]"

quality:
	black --check $(check_dirs)
	isort --check-only $(check_dirs)
	flake8 $(check_dirs)
	mypy src

style:
	black $(check_dirs)
	isort $(check_dirs)

test:
	pytest
