#!/bin/bash
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
sudo apt install python3-dev libpq-dev
python3 -m venv entorno 
python -m venv entorno
source entorno/bin/activate
pip install -r requirements.txt
entorno/bin/python manage.py runserver
