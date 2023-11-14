from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from simio_identificador import isSimian

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://vitor:Vitor2807@localhost/simian_db'
db = SQLAlchemy(app)

class DnaRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dna = db.Column(db.JSON)
    is_simian = db.Column(db.Boolean)

db.create_all()

@app.route('/simian', methods=['POST'])
def check_simian():
    data = request.get_json()
    dna = data.get('dna', [])
    is_simian_result = isSimian(dna)

    record = DnaRecord(dna=dna, is_simian=is_simian_result)
    db.session.add(record)
    db.session.commit()

    if is_simian_result:
        return jsonify({"message": "É um símio!"}), 200
    else:
        return jsonify({"message": "Não é um símio."}), 403

if __name__ == '__main__':
    app.run(debug=True)
