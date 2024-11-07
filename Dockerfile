# Use official Python image as base
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Add `daemon` user
RUN adduser --disabled-password --gecos '' daemon || true

# Set work directory
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the /app directory
COPY . /app/

# Ensure the media/uploads directory exists
RUN mkdir -p /app/media/uploads

# Set work directory to the project directory
WORKDIR /app/survey_project

# Correct `daemon` user
USER daemon

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
