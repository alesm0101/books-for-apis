# setup history

`python3 -m venv .venv`
`source .venv/bin/activate`
`python3 -m pip install django~=5.0.0`
`django-admin startproject django_project .`
`python3 manage.py startapp accounts`

`python3 manage.py makemigrations`
`python3 manage.py migrate`
`python3 manage.py createsuperuser`
`python3 manage.py runserver`
`python3 manage.py test`
`pip freeze > requirements.txt`
`python3 -m pip install djangorestframework~=3.14.0`

3.14 is requiered for django 5

`python3 -m pip install djangorestframework~=3.14.0`
`python3 manage.py startapp apis`

`python3 -m pip install whitenoise==6.0.0`
`python3 manage.py collectstatic`
`python3 -m pip install gunicorn~=20.1.0`

`python3 -m pip install 'environs[django]==9.5.0'`
`python3 -c "import secrets; print(secrets.token_urlsafe())"`

# setup
