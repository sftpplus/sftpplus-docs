#!/bin/sh
virtualenv -p python3 venv
source venv/bin/activate
venv/bin/pip install -r requirements.txt
venv/bin/sphinx-build -b html -D html_theme=integrated doc_source/ deploy
