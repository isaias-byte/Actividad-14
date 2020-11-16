from flask import Flask, jsonify, request

from conexion import crear_usuario, iniciar_sesion
from conexion import insertar_pelicula, get_peliculas, get_pelicula

app=Flask(__name__)

@app.route("/ap1/v1/usuarios", methods=["POST"])
def usuario():
    if(request.method=="POST" and request.is_json):
        try:
            data=request.get_json()
            print(data)

            if(crear_usuario(data["correo"], data["contraseña"])):
                return jsonify({"code": "Usuario registrado exitosamente"})
            else:
                return jsonify({"code": "El Usuario ya existe"})

            #return jsonify({"code": "ok"})
        except:
            return jsonify({"code": "Error al tratar de registrar Usuario"})

@app.route("/api/v1/peliculas", methods=["GET", "POST"])
@app.route("/api/v1/peliculas/<int:id>", methods=["GET"])
def peliculas(id=None):
    if(request.method=="POST" and request.is_json):
        try:
            data=request.get_json()
            print(data)
            if(insertar_pelicula(data)):
                return jsonify({"code": "ok"})
            else:
                return jsonify({"code": "no"})
        except:
            return jsonify({"code": "error"})
        return jsonify({"code": "ok"})
    elif(request.method=="GET" and id is None):
        return jsonify(get_peliculas())
    elif(request.method=="GET" and id is not None):
        return jsonify(get_pelicula(id))

@app.route("/ap1/v1/sesiones", methods=["POST"])
def sesion():
    if(request.method=="POST" and request.is_json):
        try:
            data=request.get_json()
            correo=data["correo"]
            contra=data["contraseña"]
            id, ok = iniciar_sesion(correo, contra)
            if(ok):
                return jsonify({"code": "Iniciaste Sesión", "id": id})
            else:
                return jsonify({"code": "No existe el Usuario"})
        except:
            return jsonify({"code": "Error..."})

app.run(debug=True)

