docker-compose down
docker-compose build --no-cache
docker-compose  up
docker-compose up --build

# Define the command to run the application
# docker build -t joelwembo/prodxcloud-django-web-dev:latest .
# docker push joelwembo/prodxcloud-django-web-dev:latest
# docker pull joelwembo/prodxcloud-django-web-dev:latest
# docker run -d -p 8585:8585 joelwembo/prodxcloud-django-web-dev:latest
# CMD ["gunicorn", "--bind", "0.0.0.0:8585", "multitenantsaas.wsgi:application"]
# Define the command to run the application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8585"]

