import os
import sys
from celery import Celery

path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
sys.path.append(path)

from pycrawler import app

celery = Celery(__name__, broker=os.environ['REDIS_URL'])

app.app_context().push()
