NAME := gkeeper
REGION := asia-northeast1
MAIN := main.py
PROJECT := 

.PHONY: lint
lint:
	poetry run mypy ${NAME} ${MAIN} tests
	poetry run flake8 ${NAME} ${MAIN} tests

.PHONY: test
test: lint
	poetry run pytest tests -m "not large"

.PHONY: install
install:
	poetry install

.PHONY: transcribe_poetry
transcribe_poetry:
	poetry export -f requirements.txt > requirements.txt
