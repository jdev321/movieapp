#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z movie-db 5432; do
    sleep 0.1
done

echo "PostgreSQl started"

exec "$@"