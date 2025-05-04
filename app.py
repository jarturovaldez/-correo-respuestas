from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Servidor activo.'

@app.route('/respuesta', methods=['POST'])
def recibir_respuesta():
    data = request.get_json()
    print("Respuesta recibida:", data)
    return {'status': 'ok'}, 200