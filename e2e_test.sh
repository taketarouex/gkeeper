#!/bin/bash

set -eu

export PORT=${PORT:-8080}
docker-compose up &

sleep 10

curl -f -X POST -H "Content-Type: application/json" -d '{"item":"test"}' \
    http://0.0.0.0:${PORT}/api/list/test_gkeeper/item

docker-compose down
