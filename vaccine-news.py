from flask import Flask, flash, redirect, render_template, request, session, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo='Vaccine News | Home')


@app.route('/contato')
def contato():
    return render_template('contato.html', titulo='Ajuda')

@app.route('/cuidados')
def cuidados():
    return render_template('cuidados.html', titulo='Cuidados')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo='Sobre')

 @app.route('/search', methods=['POST'])
 def search():
     search_term = request.json['searchTerm']
     results = []
    # Aqui você precisa implementar a lógica de busca em todas as páginas do seu site
    # Por exemplo, você pode usar uma biblioteca como Whoosh ou Elasticsearch para indexar e buscar conteúdo
    # Em seguida, você precisa retornar os resultados da busca como um JSON
  #   return jsonify(results=results)


if __name__ == '__main__':
    app.run(debug=True)
