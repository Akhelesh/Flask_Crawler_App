import os
import sys

path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
sys.path.append(path)

from pycrawler import celery, create_app

app = create_app()
app.app_context().push()
