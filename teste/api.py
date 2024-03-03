from flask import Flask, request, jsonify
from simian import is_simian
from simiandb import insert_dna, get_stats
app = Flask(__name__)

# Adicionar rota para o endpoint /stats
@app.route('/stats', methods=['GET'])
def stats():
    return jsonify(get_stats())

@app.route('/simian', methods=['POST'])
def detect_simian():
    dna = request.json.get('dna', [])
    result = is_simian(dna)
    insert_dna(''.join(dna), result)
    if result:
        return jsonify({"resultado":"É símio"}), 200  # DNA identificado como símio "ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG" 
    else:
        return jsonify({"resultado":"Não é símio"}), 403  # DNA não identificado como símio "ATGCGA", "CAGTGC", "TTATTT", "AGACGG", "GCGTCA", "TCACTG"

if __name__ == '__main__':
    app.run(debug=True)
