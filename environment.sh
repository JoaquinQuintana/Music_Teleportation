#!/usr/bin/env bash
sudo rm -r venv
python3 -m venv venv
source venv/bin/activate

python3 -m pip install --upgrade pip
pip install -r requirements.txt

export FLASK_APP=Monkey.py
export FLASK_ENV=development
