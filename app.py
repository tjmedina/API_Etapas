from flask import Flask, jsonify, abort
import time
from model.etapas import MODELO, ETAPAS

app = Flask(__name__)
now = time.strftime("%H:%M:%S")

@app.route('/', methods=['GET'])
@app.route('/etapas/', methods=['GET'])
def get_all_etapas():
    return jsonify(Modelo=MODELO, Etapas=ETAPAS, Começar=now)

@app.route('/etapas/<int:id>', methods=['GET'])
def una_etapa(id):
    etapa = ETAPAS.get(id)
    if etapa is None:
        return jsonify({'error': 'Esta fase não existe'}), 404
    return jsonify(Modelo=MODELO, Etapa=etapa, Começar=now )

def unaetapa(id):
    return next((e for e in ETAPAS if e['id'] == id), None)

def etapa_valida(etapa):
    for key in etapa.keys():
        if key != 'ETAPA':
            return False
    return True

if __name__ == "__main__":
    app.run(debug=True)