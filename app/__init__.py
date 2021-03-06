from config import *
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.via import Via

app = Flask(__name__ )
#app.config.from_object('config.BaseConfig')
app.config.from_object('config.DevelopmentConfig')
app.config['VIA_ROUTES_MODULE'] = 'config.routes'
db = SQLAlchemy(app)
via = Via()
via.init_app(app, routes_name='urls')
