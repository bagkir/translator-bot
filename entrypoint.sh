#!/bin/sh
alembic upgrade head
cd app/
exec python3 ./main.py