from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config('config.py')

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template()