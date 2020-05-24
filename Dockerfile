FROM python:3.7-buster as builder

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry gunicorn keyrings.cryptfile

RUN poetry config virtualenvs.create false && \
    poetry install

FROM python:3.7-slim-buster as runner

COPY --from=builder /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

COPY gkeeper/ /app/gkeeper/
COPY app.py /app

WORKDIR /app

EXPOSE $PORT

CMD exec gunicorn --bind :$PORT --workers 1 --preload app:app
