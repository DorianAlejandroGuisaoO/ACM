from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados (en lugar de BD por ahora)
messages = [
    {"id": 1, "author": "Usuario A", "text": "Hola! me interesa el empleo", "time": "2025-09-15 10:00"},
    {"id": 2, "author": "Usuario B", "text": "Sigue disponible el empleo?", "time": "2025-09-15 10:30"},
    {"id": 3, "author": "Usuario C", "text": "Contratan recien graduados?", "time": "2025-09-15 11:00"}
]

# Endpoint para listar mensajes
@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

# Endpoint para responder
@app.route("/reply", methods=["POST"])
def reply():
    data = request.get_json()
    text = data.get("text", "").lower()

    if "interesa" in text:
        response = "¡Gracias por tu interés! La vacante está abierta."
    elif "disponible" in text:
        response = "Sí, la posición sigue disponible."
    elif "graduad" in text:
        response = "Sí, aceptamos recién graduados."
    else:
        response = "Gracias por tu mensaje, pronto te daremos más información."

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
