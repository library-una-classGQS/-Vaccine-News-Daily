from flask import render_template
from projeto import app

@app.route('/')
def index():
    return render_template('templates/index.html', titulo='Vaccine News | Home')


@app.route('/contato')
def contato():
    return render_template('templates/contato.html', titulo='Ajuda')

@app.route('/cuidados')
def cuidados():
    video = 'https://www.youtube.com/watch?v=jKGda3zw3m4'
    return render_template('templates/cuidados.html', titulo='Cuidados', video=video)

@app.route('/sobre')
def sobre():
    return render_template('templates/sobre.html', titulo='Sobre')
