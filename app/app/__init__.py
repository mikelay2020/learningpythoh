from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

from app import models
from app import views
