from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'clave_secreta_segura'
jwt = JWTManager(app)

# Simulación de base de datos
users_db = {}
establecimientos = []
comentarios = []
valoraciones = []

# Rutas de Autenticación
@app.route('/auth/register', methods=['POST'])
def register():
    data = request.json
    if data['email'] in users_db:
        return jsonify({"error": "Usuario ya registrado"}), 400
    users_db[data['email']] = {"nombre": data['nombre'], "password": data['password']}
    return jsonify({"message": "Usuario registrado con éxito"}), 201

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    user = users_db.get(data['email'])
    if not user or user['password'] != data['password']:
        return jsonify({"error": "Credenciales inválidas"}), 401
    token = create_access_token(identity=data['email'])
    return jsonify({"access_token": token}), 200

@app.route('/auth/logout', methods=['POST'])
@jwt_required()
def logout():
    return jsonify({"message": "Cierre de sesión exitoso"}), 200

# Rutas de Usuarios
@app.route('/usuarios/<int:id>', methods=['GET'])
@jwt_required()
def obtener_usuario(id):
    user = {"id": id, "nombre": f"Usuario{id}"}
    return jsonify(user), 200

@app.route('/usuarios/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_usuario(id):
    data = request.json
    return jsonify({"message": f"Usuario {id} actualizado con éxito"}), 200

@app.route('/usuarios/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_usuario(id):
    return jsonify({"message": f"Usuario {id} eliminado con éxito"}), 200

@app.route('/usuarios/search', methods=['GET'])
@jwt_required()
def buscar_usuarios():
    query = request.args.get('q', '')
    resultados = [u for u in users_db.values() if query.lower() in u['nombre'].lower()]
    return jsonify(resultados), 200

# Rutas de Establecimientos
@app.route('/establecimientos', methods=['GET'])
def obtener_establecimientos():
    return jsonify(establecimientos), 200

@app.route('/establecimientos/<int:id>', methods=['GET'])
def obtener_establecimiento(id):
    establecimiento = next((e for e in establecimientos if e['id'] == id), None)
    if not establecimiento:
        return jsonify({"error": "Establecimiento no encontrado"}), 404
    return jsonify(establecimiento), 200

@app.route('/establecimientos', methods=['POST'])
@jwt_required()
def agregar_establecimiento():
    data = request.json
    establecimiento = {"id": len(establecimientos) + 1, "nombre": data['nombre'], "ubicacion": data['ubicacion']}
    establecimientos.append(establecimiento)
    return jsonify({"message": "Establecimiento añadido con éxito", "establecimiento": establecimiento}), 201

@app.route('/establecimientos/<int:id>', methods=['PUT'])
@jwt_required()
def editar_establecimiento(id):
    data = request.json
    establecimiento = next((e for e in establecimientos if e['id'] == id), None)
    if not establecimiento:
        return jsonify({"error": "Establecimiento no encontrado"}), 404
    establecimiento.update(data)
    return jsonify({"message": "Establecimiento actualizado con éxito", "establecimiento": establecimiento}), 200

@app.route('/establecimientos/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_establecimiento(id):
    establecimiento = next((e for e in establecimientos if e['id'] == id), None)
    if not establecimiento:
        return jsonify({"error": "Establecimiento no encontrado"}), 404
    establecimientos.remove(establecimiento)
    return jsonify({"message": "Establecimiento eliminado con éxito"}), 200

@app.route('/establecimientos/search', methods=['GET'])
def buscar_establecimientos():
    query = request.args.get('q', '')
    resultados = [e for e in establecimientos if query.lower() in e['nombre'].lower()]
    return jsonify(resultados), 200

# Rutas de Comentarios
@app.route('/establecimientos/<int:id>/comentarios', methods=['POST'])
@jwt_required()
def agregar_comentario(id):
    data = request.json
    comentario = {"id": len(comentarios) + 1, "texto": data['texto'], "usuario": "UsuarioX"}
    comentarios.append(comentario)
    return jsonify({"message": "Comentario añadido con éxito", "comentario": comentario}), 201

@app.route('/establecimientos/<int:id>/comentarios/<int:comentario_id>', methods=['PUT'])
@jwt_required()
def editar_comentario(id, comentario_id):
    data = request.json
    comentario = next((c for c in comentarios if c['id'] == comentario_id), None)
    if not comentario:
        return jsonify({"error": "Comentario no encontrado"}), 404
    comentario.update(data)
    return jsonify({"message": "Comentario actualizado con éxito", "comentario": comentario}), 200

@app.route('/establecimientos/<int:id>/comentarios/<int:comentario_id>', methods=['DELETE'])
@jwt_required()
def eliminar_comentario(id, comentario_id):
    comentario = next((c for c in comentarios if c['id'] == comentario_id), None)
    if not comentario:
        return jsonify({"error": "Comentario no encontrado"}), 404
    comentarios.remove(comentario)
    return jsonify({"message": "Comentario eliminado con éxito"}), 200

@app.route('/establecimientos/<int:id>/comentarios', methods=['GET'])
def obtener_comentarios(id):
    return jsonify(comentarios), 200

# Rutas de Valoraciones
@app.route('/establecimientos/<int:id>/valoraciones', methods=['POST'])
@jwt_required()
def agregar_valoracion(id):
    data = request.json
    valoracion = {"id": len(valoraciones) + 1, "puntuacion": data['puntuacion'], "usuario": "UsuarioX"}
    valoraciones.append(valoracion)
    return jsonify({"message": "Valoración añadida con éxito", "valoracion": valoracion}), 201

@app.route('/establecimientos/<int:id>/valoraciones/<int:valoracion_id>', methods=['PUT'])
@jwt_required()
def editar_valoracion(id, valoracion_id):
    data = request.json
    valoracion = next((v for v in valoraciones if v['id'] == valoracion_id), None)
    if not valoracion:
        return jsonify({"error": "Valoración no encontrada"}), 404
    valoracion.update(data)
    return jsonify({"message": "Valoración actualizada con éxito", "valoracion": valoracion}), 200

@app.route('/establecimientos/<int:id>/valoraciones/<int:valoracion_id>', methods=['DELETE'])
@jwt_required()
def eliminar_valoracion(id, valoracion_id):
    valoracion = next((v for v in valoraciones if v['id'] == valoracion_id), None)
    if not valoracion:
        return jsonify({"error": "Valoración no encontrada"}), 404
    valoraciones.remove(valoracion)
    return jsonify({"message": "Valoración eliminada con éxito"}), 200

@app.route('/establecimientos/<int:id>/valoraciones', methods=['GET'])
def obtener_valoraciones(id):
    return jsonify(valoraciones), 200

@app.route('/valoraciones/search', methods=['GET'])
def buscar_valoraciones():
    query = request.args.get('q', '')
    resultados = [v for v in valoraciones if query.lower() in str(v.get('puntuacion', '')).lower()]
    return jsonify(resultados), 200

if __name__ == '__main__':
    app.run(debug=True)
