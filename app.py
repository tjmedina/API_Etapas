from flask import Flask, jsonify, abort
import time
from model.etapas import MODELO, ETAPAS


app = Flask(__name__)

now = time.strftime("%H:%M:%S")

@app.route('/', methods=['GET'])
@app.route('/etapas', methods=['GET'])
def get_all_etapas():
    return jsonify(Modelo=MODELO, Etapas=ETAPAS, Começar=now)

@app.route('/etapas/<int:id>', methods=['GET'])
def una_etapa(id):
    etapa = ETAPAS.get(id)
    if not etapa:
        abort(404)
    return jsonify(Modelo=MODELO, Etapa=etapa, Começar=now )

if __name__ == "__main__":
    app.run(debug=True)
