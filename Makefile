.PHONY: lint
lint:
	poetry run flake8 --exclude .venv

.PHONY: test
test: lint
	poetry run pytest

.PHONY: install
install:
	poetry install

.PHONY: deploy
deploy:
	poetry export -f requirements.txt > requirements.txt
	gcloud functions deploy add-keep-shopping-list \
			--region asia-northeast1 \
			--entry-point main \
			--set-env-vars KEEP_PASSWORD=${KEEP_PASSWORD} \
			--trigger-http