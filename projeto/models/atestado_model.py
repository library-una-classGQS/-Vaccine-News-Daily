from projeto import db


class Atestado(db.Model):
    __tablename__ = 'atestado'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    cid = db.Column(db.Integer, nullable=False)
    tempo = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)

    def __init__(self, nome, cid, tempo, data, hora):
        self.nome = nome
        self.cid = cid
        self.tempo = tempo
        self.data = data
        self.hora = hora

    def __repr__(self):
        return '<Atestado'
