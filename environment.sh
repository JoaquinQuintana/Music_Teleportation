#!/usr/bin/env bash
sudo rm -r venv
python3 -m venv venv
python -m pip install --upgrade pip
pip install -r requirements.txt
source venv/bin/activate
export FLASK_APP=Monkey.py
export FLASK_ENV=development
