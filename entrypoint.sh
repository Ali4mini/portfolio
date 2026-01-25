#!/bin/sh

# If the command is to run the server, wait for the DB first
if [ "$1" = "python" ]; then
    echo "Waiting for postgres..."

    while ! nc -z db 5432; do
      sleep 0.1
    done

    echo "PostgreSQL started"

    python manage.py migrate --noinput
    
    python manage.py collectstatic --noinput

fi

exec "$@"
