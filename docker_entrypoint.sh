#!/usr/bin/env bash

echo "Look init"
flask db init

echo "Start Migrate"
flask db migrate

echo "Start Upgrade"
flask db upgrade

python wsgi.py 127.0.0.1:5000:5000
