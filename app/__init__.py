# app/__init__.py

import spotify_client

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load configs
app.config.from_pyfile('config.py')

# db initialization
db = SQLAlchemy()
db.init_app(app)

# Initialize login manager.
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"

from app import models

# Initialize migration handler.
migrate = Migrate(app, db)

# Load the views as blueprints.
from .recommendations import recommendations as recommendations_blueprint
app.register_blueprint(recommendations_blueprint)

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)
