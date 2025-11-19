from flask import Flask, request, jsonify
from calculator.core import operate

app = Flask(__name__)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/api/calc", methods=["POST"])
def calc():
    """
    Espera un JSON:
    {
      "a": 10,
      "b": 5,
      "op": "add" | "sub" | "mul" | "div"
    }
    """
    data = request.get_json(silent=True) or {}
    try:
        a = float(data.get("a"))
        b = float(data.get("b"))
        op = str(data.get("op"))
    except (TypeError, ValueError):
        return jsonify({"error": "Datos inválidos"}), 400

    try:
        result = operate(a, b, op)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
