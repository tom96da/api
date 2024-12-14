#!/bin/sh

if [ "$FLASK_ENV" = "development" ]; then
    export FLASK_DEBUG=1
    flask run --host=0.0.0.0
else
    gunicorn 'wsgi:app' --bind :5000
fi
