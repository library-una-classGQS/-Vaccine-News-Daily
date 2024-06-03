from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
