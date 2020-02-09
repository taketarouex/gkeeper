NAME := gkeeper
REGION := asia-northeast1
MAIN := main.py

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

.PHONY: deploy
deploy: test
	poetry export -f requirements.txt > requirements.txt
	gcloud functions deploy ${NAME} \
			--region ${REGION} \
			--entry-point main \
			--set-env-vars KEEP_PASSWORD=${KEEP_PASSWORD} \
			--runtime python37 \
			--trigger-http