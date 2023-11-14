from flask import Flask, request, jsonify

from simio_identificador import isSimian

app = Flask(__name__)

@app.route('/simian', methods=['POST'])
def check_simian():
    data = request.get_json()
    dna = data.get('dna', [])
    
    if isSimian(dna):
        return jsonify({"message": "É um símio!"}), 200
    else:
        return jsonify({"message": "Não é um símio."}), 403

# Exemplo de execução
if __name__ == '__main__':
    app.run(debug=True)
