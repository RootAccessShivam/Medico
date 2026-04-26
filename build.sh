#!/usr/bin/env bash
set -e

pip install -r requirements.txt
python manage.py migrate

# create superuser if not exists
echo "from django.contrib.auth import get_user_model
User = get_user_model()
username='admin'
password='admin123'
email='admin@gmail.com'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('SUPERUSER_CREATED')
else:
    print('SUPERUSER_EXISTS')
" | python manage.py shell

python manage.py collectstatic --noinput