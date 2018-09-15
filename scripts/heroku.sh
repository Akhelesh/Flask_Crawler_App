python3 manage.py db upgrade

celery worker -A pycrawler.backgroundtasks.celery.celery --loglevel=info -Ofair &
gunicorn run:app