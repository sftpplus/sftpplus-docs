#!/bin/sh
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
sphinx-build -b html -D html_theme=integrated doc_source/ deploy
