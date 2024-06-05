from flask import Flask, flash, redirect, render_template, request, session, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
import json

path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)





@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    pesquisa = request.form["search-input"]
    resultados = []

    with open(f'{path}/data/artigos.json', 'r', encoding='utf-8') as file:
        artigos = json.load(file)

    for artigo in artigos:
        if pesquisa.lower() in artigo['conteudo'].lower() or pesquisa.lower() in artigo['titulo'].lower():
            resultados.append(artigo)

    if not resultados:
        return redirect(url_for('erro'))

    return render_template('resultados.html', resultados=resultados)


@app.route('/erro')
def erro():
    return render_template('erro.html')


@app.route('/forum')
def forum():
    return render_template('forum.html', titulo='forum')




@app.route('/search', methods=['POST'])
def search():
    data = request.json
    search_term = data.get('searchTerm').lower()
    results = []
    
    if 'hpv' in search_term:
        results.append({
            "titulo": "HPV",
            "conteudo": "Ministerio da saude anuncia vacinas em dose unica contra hpv, veja como se instreves",
            "imagem": "hpv.jpg"
        })
    if 'dengue' in search_term:
        results.append({
            "titulo": "Dengue",
            "conteudo": "Ministerio da Saude discute estratégia para distribuição de vacina contra Dengue",
            "imagem": "dengue.jpg"
        })
    
    return jsonify({"results": results})

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


@app.route('/inscrever')
def inscrever():
    return render_template('inscrever.html', titulo='inscrever')


if __name__ == '__main__':
    app.run(debug=True)
