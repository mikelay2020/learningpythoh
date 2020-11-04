
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

# ...
#from flask_moment import Moment

#app = Flask(__name__)
# ...
#moment = Moment(app)
