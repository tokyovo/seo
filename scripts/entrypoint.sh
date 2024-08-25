#!/bin/bash

# Function to wait for the database to be ready
wait_for_db() {
    echo "Waiting for the database to be ready..."
    while ! nc -z db 5432; do   
      sleep 0.1  # wait for 1/10 of the second before check again
    done
    echo "Database is ready!"
}

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Wait for the database to be ready
wait_for_db

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn --workers=3 --bind :8000 agent.wsgi:application
