from flask import Flask
from .config import DevConfig
app = Flask (__name__)
# set up the configuration
app.config.from_object(DevConfig)
from app import views