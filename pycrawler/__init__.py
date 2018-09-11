import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from celery import Celery


app = Flask(__name__)
app.config.from_object(os.environ['APP_CONFIG'])

bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
db = SQLAlchemy(app)
mail = Mail(app)

celery = Celery(__name__)
celery.config_from_object(os.environ['APP_SETTINGS'] + '.CeleryConfig')


from pycrawler.main.routes import main
from pycrawler.users.routes import users
from pycrawler.results.routes import results
from pycrawler.errors.handlers import errors
app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(results)
app.register_blueprint(errors)