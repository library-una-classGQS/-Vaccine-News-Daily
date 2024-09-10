from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Simulação de banco de dados para armazenar os agendamentos
agendamentos = []

# Rota para verificar disponibilidade de data e hora
@app.route('/verificar_disponibilidade', methods=['POST'])
def verificar_disponibilidade():
    data = request.json.get('data')
    hora = request.json.get('hora')
    data_hora_nova = f"{data} {hora}"
    
    for agendamento in agendamentos:
        data_hora_existente = f"{agendamento['data']} {agendamento['hora']}"
        if data_hora_nova == data_hora_existente:
            return jsonify({"disponivel": False})
    
    return jsonify({"disponivel": True})

# Rota para adicionar um novo agendamento
@app.route('/agendar', methods=['POST'])
def agendar():
    nome = request.json.get('nome')
    email = request.json.get('email')
    data = request.json.get('data')
    hora = request.json.get('hora')
    especialidade = request.json.get('especialidade')
    sexo = request.json.get('sexo')
    descricao = request.json.get('descricao')

    # Verifica se a data e hora já estão ocupadas
    for agendamento in agendamentos:
        if agendamento['data'] == data and agendamento['hora'] == hora:
            return jsonify({"status": "error", "message": "Data e hora já agendadas!"})

    # Adiciona o novo agendamento
    agendamentos.append({
        "nome": nome,
        "email": email,
        "data": data,
        "hora": hora,
        "especialidade": especialidade,
        "sexo": sexo,
        "descricao": descricao
    })

    return jsonify({"status": "success", "message": "Consulta agendada com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
