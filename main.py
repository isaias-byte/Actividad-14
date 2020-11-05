from flask import Flask, jsonify, request

from conexion import crear_usuario, iniciar_sesion

app=Flask(__name__)

@app.route("/ap1/v1/usuarios", methods=["POST"])
def usuario():
    if(request.method=="POST" and request.is_json):
        try:
            data=request.get_json()
            print(data)

            if(crear_usuario(data["correo"], data["contraseña"])):
                return jsonify({"code": "ok"})
            else:
                return jsonify({"code": "existe"})

            return jsonify({"code": "ok"})
        except:
            return jsonify({"code": "error"})

@app.route("/ap1/v1/sesiones", methods=["POST"])
def sesion():
    if(request.method=="POST" and request.is_json):
        try:
            data=request.get_json()
            correo=data["correo"]
            contra=data["contraseña"]
            id, ok = iniciar_sesion(correo, contra)
            if(ok):
                return jsonify({"code": "ok", "id": id})
            else:
                return jsonify({"code": "no existe"})
        except:
            return jsonify({"code": "error"})

app.run(debug=True)

