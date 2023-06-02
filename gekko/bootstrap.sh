#!/bin/sh
export FLASK_APP=./src/app.py
pipenv run flask --debug run -h 0.0.0.0