# Django Dockerfile to build the Docker image for the production environment
# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=multitenantsaas.settings

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc \
    build-essential \
    python3-psycopg2 \
    curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /djangoapp

# Copy only requirements file to leverage Docker cache
COPY requirements.txt /djangoapp/

# Install Python dependencies
RUN pip install --upgrade pip setuptools && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code and static files into the container
COPY . /djangoapp/
COPY .env /djangoapp/
COPY staticfiles /djangoapp/staticfiles/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run database migrations only if the database is available and ready
# RUN python manage.py makemigrations users && \
#     python manage.py migrate users

RUN python manage.py makemigrations && \
    python manage.py migrate    

# Change ownership of the application directory
RUN chown -R root:root /djangoapp

# Expose necessary ports
EXPOSE 8585
EXPOSE 443
EXPOSE 80
EXPOSE 80/tcp
EXPOSE 8585
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8585", "--workers", "4", "--threads", "4", "multitenantsaas.wsgi:application"]

# # Run the entry point script
# ENTRYPOINT ["./entrypoint.sh"]