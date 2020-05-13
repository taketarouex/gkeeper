NAME := gkeeper
REGION := asia-northeast1
MAIN := main.py
PROJECT := 

.PHONY: lint
lint:
	poetry run mypy ${NAME} ${MAIN}
	poetry run flake8 ${NAME} ${MAIN}

.PHONY: test
test: lint
	poetry run pytest ${NAME}/tests -m "not large"

.PHONY: install
install:
	poetry install

.PHONY: transcribe_poetry
transcribe_poetry:
	poetry export -f requirements.txt > requirements.txt
