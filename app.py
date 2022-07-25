from flask import Flask, jsonify, abort
import time
from model.etapas import MODELO, ETAPAS
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'minha_chave_secreta'
csrf = CSRFProtect(app)

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
