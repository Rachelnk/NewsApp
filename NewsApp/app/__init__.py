from flask import Flask
from .config import DevConfig , config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap ()
def create_app(config_name):
  app = Flask (__name__)
  # Creating the app configurations
  app.config.from_object(config_options[config_name])
  # Initializing flask extensions
  bootstrap.init_app(app)
  # Will add the views and forms

  return app
# set up the configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')
#  initialize flask extensions
# bootstrap = Bootstrap(app)
# from app import views
# from app import error