from projeto import db

class Medico(db.Model):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_medico = db.Column(db.String(100), nullable=False)
    crm = db.Column(db.Integer, nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)