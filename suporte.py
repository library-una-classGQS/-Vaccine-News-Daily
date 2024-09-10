from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Configure a sua chave de API da OpenAI
openai.api_key = 'sua-chave-de-api'

@app.route('/support', methods=['POST'])
def support():
    user_message = request.json.get('message')

    # Envie a mensagem do usuário para o ChatGPT
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # ou o engine GPT mais recente disponível
            prompt=user_message,
            max_tokens=150
        )

        # Obtenha a resposta do ChatGPT
        chatgpt_response = response.choices[0].text.strip()

        return jsonify({'response': chatgpt_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
