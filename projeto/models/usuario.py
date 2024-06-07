from projeto import db


class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = db.Column(db.String(20), nullable=False)
    usuario = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.Integer, nullable=False)

    def __init__(self, nome, usuario, email, senha):
        self.nome = nome
        self.usuario = usuario
        self.email = email
        self.senha = senha

