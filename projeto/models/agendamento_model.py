from projeto import db


class Agendamento(db.Model):
    __tablename__ = 'agendamento'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    agendamento_form = db.Column(db.String(100), nullable=False)
    unidade = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)

    def __init__(self, nome, email, especialidade, sexo, data, hora, agendamento_form, unidade, descricao):
        self.nome = nome
        self.email = email
        self.especialidade = especialidade
        self.sexo = sexo
        self.data = data
        self.hora = hora
        self.agendamento_form = agendamento_form
        self.unidade = unidade
        self.descricao = descricao

    def __repr__(self):
        return '<Agendamento: {}>'.format(self.nome)
