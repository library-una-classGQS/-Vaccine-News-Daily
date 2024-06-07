import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=f"{path}/../templates", static_folder=f"{path}/../static")
app.config.from_object("config")

db = SQLAlchemy(app)

from projeto.models.usuario import Usuario
