from flask import Flask, request, jsonify
from calcular_nota import verficar_nota
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    ap1 = float(data.get('ap1', 0))
    ap2 = float(data.get('ap2', 0))
    ac = float(data.get('ac', 0))
    resultado = verficar_nota(ap1, ap2, ac)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
