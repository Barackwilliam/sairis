# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for psycopg2 and Django
RUN apt-get update && \
    apt-get install -y libpq-dev python3-dev && \
    apt-get clean

# Copy the requirements file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the container
COPY . .

# Expose the port the app will run on
EXPOSE 8000

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1

# Command to run your app (you can use 'python manage.py runserver' for development)
# For production, use Gunicorn (recommended for production environments)
CMD ["gunicorn", "ecommerce.wsgi:application", "--bind", "0.0.0.0:8000"]
