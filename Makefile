.PHONY: install
install:
	poetry install

.PHONY: fix
fix:
	poetry run black .
	poetry run isort .

.PHONY: quality
lint:
	poetry run black --check .
	poetry run isort --check .
	poetry run flake8 .
	poetry run pylint **/*.py
	poetry run mypy .

.PHONY: test
test:
	poetry run pytest --cov cocktail_opt
