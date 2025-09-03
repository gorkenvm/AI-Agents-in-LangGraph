.PHONY: install lint fix test run

install:
	pip install -r requirements.txt -r requirements-dev.txt
	pre-commit install

lint:
	ruff check . && black --check . && isort --check-only .

fix:
	ruff check --fix . && black . && isort .

test:
	pytest -q

run:
	jupyter lab
