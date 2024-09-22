#!/usr/bin/env sh
python manage.py makemigrations

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 3
done

python manage.py collectstatic --noinput
python manage.py create_default_superuser
gunicorn multitenantsaas.wsgi --bind 0.0.0.0:8585 --workers 4 --threads 4
# for debug
# python manage.py runserver
# python manage.py runserver 0.0.0.0:8585