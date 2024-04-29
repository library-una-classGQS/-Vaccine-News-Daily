from flask import Flask, flash, redirect, render_template, request, session, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os


path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')


if __name__ == '__main__':
    app.run(debug=True)
