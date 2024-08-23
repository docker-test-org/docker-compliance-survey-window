# Use official Python image as base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

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

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
