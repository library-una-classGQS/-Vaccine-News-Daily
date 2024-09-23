from projeto import db


class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = db.Column(db.String(20), nullable=False)
    cpf_cnpj = db.Column(db.BigInteger, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cartao_sus = db.Column(db.Integer, nullable=False)
    senha = db.Column(db.String(20), nullable=False)

    def __init__(self, nome, cpf_cnpj, email, senha):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.email = email
        self.senha = senha

    def __repr__(self):
        return f"Usuario(nome={self.nome})"
