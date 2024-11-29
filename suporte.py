from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Configure a sua chave de API da OpenAI
openai.api_key = ''
openai.api_key = os.getenv("")

@app.route('/support', methods=['POST'])
def support():
    user_message = request.json.get('message')

    # Envie a mensagem do usuário para o ChatGPT
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Modelo atualizado
            prompt=user_message,
            max_tokens=150,
            timeout=10  # Timeout de 10 segundos
        )

        # Obtenha a resposta do ChatGPT
        chatgpt_response = response.choices[0].text.strip()

        return jsonify({'response': chatgpt_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
