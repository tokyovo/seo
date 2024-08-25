# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev netcat-openbsd \
    && apt-get install -y --no-install-recommends libgl1-mesa-glx libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
# Copy requirements.txt to a different directory, for example, /deploy
COPY requirements.txt /deploy/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /deploy/requirements.txt

# Copy the agent project directory to /app
COPY agent /app/

# Copy entrypoint script to a different directory, such as /deploy, and ensure it's executable
COPY scripts/entrypoint.sh /deploy/entrypoint.sh
RUN chmod +x /deploy/entrypoint.sh

# Define the entry point script from the /deploy directory
ENTRYPOINT ["/deploy/entrypoint.sh"]
