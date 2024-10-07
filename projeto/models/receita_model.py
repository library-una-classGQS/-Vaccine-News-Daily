from projeto import db


class Receita(db.Model):
    __tablename__ = 'receita'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_paciente = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(20), nullable=False)
    data_receita = db.Column(db.Date, nullable=False)
    medicamentos = db.Column(db.String(100), nullable=False)
    dosagem = db.Column(db.String(100), nullable=False)
    instrucoes = db.Column(db.String(100), nullable=False)
    info_medico = db.Column(db.String(100), nullable=False)
    crm = db.Column(db.Integer, nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)

    def __init__(self, nome_paciente, idade, sexo, data_receita, medicamentos, dosagem, instrucoes, info_medico, crm,
                 especialidade):
        self.nome_paciente = nome_paciente
        self.idade = idade
        self.sexo = sexo
        self.data_receita = data_receita
        self.medicamentos = medicamentos
        self.dosagem = dosagem
        self.instrucoes = instrucoes
        self.info_medico = info_medico
        self.crm = crm
        self.especialidade = especialidade

    def __repr__(self):
        return '<Receita'
