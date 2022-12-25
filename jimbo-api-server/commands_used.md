to start project:  
```
django-admin startproject core .
```
to create server app:  
```
python manage.py startapp jimbo_server
```
to create api:  
```
python manage.py startapp jimbo_api
```
to run server:  
```
python manage.py runserver
```
to save requirements:  
```
pip freeze > requirements.txt
```
to create migrations to db:  
```
python manage.py makemigrations
```
to migrate models to db:  
```
python manage.py migrate
```
to create superuser:
```
python manage.py createsuperuser
```