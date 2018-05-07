#!/bin/bash
# For us in Docker

# Collect static files
echo "Collect static files"
python3 manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate
python3 manage.py migrate --database "datadrop_business"

# Start server
echo "Starting server"
python3 manage.py runserver 0.0.0.0:8000
