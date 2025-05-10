# Use slim Python base image
FROM python:3.12-slim

# Environment settings to reduce noise and enable real-time logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    netcat-openbsd curl sqlite3 \
    && apt-get clean


# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .


# Collect static files (can be overridden in compose or entrypoint)
RUN python manage.py collectstatic --noinput

# Use Gunicorn to run the Django app
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
