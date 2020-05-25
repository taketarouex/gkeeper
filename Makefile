.PHONY: lint test install build run

NAME := gkeeper
REGION := asia-northeast1

lint:
	poetry run mypy ${NAME} tests app.py
	poetry run flake8 ${NAME} tests app.py

test: lint
	poetry run pytest tests -m "not large"

install:
	poetry install

build:
	docker-compose build app

run:
	docker-compose run --service-ports app

stop:
	docker-compose stop