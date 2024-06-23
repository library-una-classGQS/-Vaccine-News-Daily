import json
import os
from functools import wraps

from flask import flash, g, redirect, render_template, request, session, url_for

from projeto import app, db, migrate
from projeto.models.usuario import Usuario

path = os.path.dirname(os.path.abspath(__file__))


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("usuario_logado"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


@app.before_request
def before_request():
    g.logado = session.get("usuario_logado", False)
    g.nome = session.get("nome", None)
    g.email = session.get("email", None)
    g.cpf_cnpj = session.get("cpf_cnpj", None)


@app.route("/")
def index():
    return render_template("index.html", titulo="Vaccine News | Home")


@app.route("/pesquisar", methods=["POST"])
def pesquisar():
    pesquisa = request.form["search-input"]
    resultados = []

    with open(f"{path}/data/artigos.json", "r", encoding="utf-8") as file:
        artigos = json.load(file)

    for artigo in artigos:
        if (
            pesquisa.lower() in artigo["conteudo"].lower()
            or pesquisa.lower() in artigo["titulo"].lower()
        ):
            resultados.append(artigo)

    if not resultados:
        return redirect(url_for("erro"))

    return render_template("resultados.html", resultados=resultados)


@app.route("/cadastrar", methods=["POST",])
def cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    cpf_cnpj = request.form["cpf_cnpj"]
    senha = request.form["senha"]

    usuario = (
        Usuario.query.filter_by(email=email).first()
        or Usuario.query.filter_by(cpf_cnpj=cpf_cnpj).first()
    )

    if usuario:
        flash(f"Usuário já cadastrado!")
        return redirect(url_for("inscrever"))

    novo_usuario = Usuario(nome=nome, email=email, cpf_cnpj=cpf_cnpj, senha=senha)
    db.session.add(novo_usuario)
    db.session.commit()

    return redirect(url_for("index"))


@app.route(
    "/autenticar",
    methods=[
        "POST",
    ],
)
def autenticar():
    email_login = request.form["username"]
    senha = request.form["password"]

    usuario = Usuario.query.filter_by(email=email_login, senha=senha).first()

    if not usuario:
        return redirect(url_for("login"))
    else:
        session["usuario_logado"] = True
        session["nome"] = usuario.nome
        session["email"] = usuario.email
        session["cpf_cnpj"] = usuario.cpf_cnpj

        return redirect(url_for("index"))


@app.route("/forum")
@login_required
def forum():
    return render_template("forum.html", titulo="Fórum")


@app.route("/contato")
def contato():
    return render_template("contato.html", titulo="Ajuda")


@app.route("/cuidados")
def cuidados():
    return render_template("cuidados.html", titulo="Cuidados")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html", titulo="Sobre")


@app.route("/inscrever")
def inscrever():
    return render_template("inscrever.html", titulo="inscrever")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/erro")
def erro():
    return render_template("erro.html")



if __name__ == "__main__":
    app.run(debug=True)
