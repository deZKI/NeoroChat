#!/bin/sh

# Выполнение миграций
python manage.py migrate users
python manage.py migrate --noinput
echo "Migrations"

# Запуск start_bott
python manage.py start_bot &
echo "start_bott"

# Start server
echo "Starting server"
python manage.py runserver
exec "$@"
