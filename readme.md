# Example Celery Progress Bar
## start rabbitmq-broker 
```
docker compose up -d
```
## Init Django project
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
## Start Celery
```
celery -A core worker -l INFO
```