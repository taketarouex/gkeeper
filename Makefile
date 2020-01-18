.PHONY: lint
lint:
	poetry run mypy main.py tests lib
	poetry run flake8 --exclude .venv

.PHONY: test
test: lint
	poetry run pytest -m "not large"

.PHONY: install
install:
	poetry install

.PHONY: deploy
deploy: test
	poetry export -f requirements.txt > requirements.txt
	gcloud functions deploy add-keep-shopping-list \
			--region asia-northeast1 \
			--entry-point main \
			--set-env-vars KEEP_PASSWORD=${KEEP_PASSWORD} \
			--trigger-http