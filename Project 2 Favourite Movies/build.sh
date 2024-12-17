#!/usr/bin/env bash
# exit on error
set -o errexit

cd "Project 2 Favourite Movies"

pip install -r requirements.txt
python3 manage.py collectstatic --no-input
python3 manage.py migrate