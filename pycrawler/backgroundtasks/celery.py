import os
import sys

path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
sys.path.append(path)

from pycrawler import celery, app

app.app_context().push()
