#!/bin/bash
# start.sh – Railpack uchun Django deploy script

# 1. Virtual environment ishlatilsa uni faollashtirish (agar kerak bo‘lsa)
# source venv/bin/activate

# 2. Django static fayllarni to‘plab olish
echo "Collecting static files..."
python manage.py collectstatic --noinput

# 3. Migrationlarni qo‘llash
echo "Applying database migrations..."
python manage.py migrate

# 4. Gunicorn bilan serverni ishga tushirish
echo "Starting Gunicorn server..."
exec gunicorn todo_project.wsgi:application --bind 0.0.0.0:$PORT


chmod +x start.sh
