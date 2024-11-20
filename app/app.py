from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from app.services.geolocalizacion import servicio_geolocalizacion
from app.services.recomendaciones import servicio_recomendaciones
from app.services.establecimiento import servicio_establecimientos
from app.services.usuario import servicio_usuarios, ErrorUsuarioExistente
from app.services.valoracion import servicio_valoraciones
from utils.logging_config import logger, log_request

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'clave_secreta_segura'
jwt = JWTManager(app)

# Simulación de base de datos
establecimientos = servicio_geolocalizacion.establecimientos
comentarios = []
valoraciones = []

### Autenticación
@app.route('/auth/register', methods=['POST'])
@log_request
def register():
    data = request.json
    if not data or "email" not in data or "password" not in data:
        logger.warning("Datos incompletos en /auth/register")
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    try:
        message = servicio_usuarios.registrar_usuario(data['email'], data['password'])
        logger.info(f"Usuario registrado: {data['email']}")
        return jsonify({"message": message}), 201
    except ValueError as e:
        logger.warning(f"Error de validación: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Error interno: {e}")
        return jsonify({"error": "Error interno en el servidor"}), 500


@app.route('/auth/login', methods=['POST'])
@log_request
def login():
    data = request.json
    if not data or "email" not in data or "password" not in data:
        logger.warning("Datos incompletos en /auth/login")
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    try:
        user = servicio_usuarios.obtener_usuario(data['email'])
        if not user or user["contrasena"] != data['password']:
            logger.warning("Credenciales inválidas")
            return jsonify({"error": "Credenciales inválidas"}), 401
        token = create_access_token(identity=data['email'])
        logger.info(f"Token generado para: {data['email']}")
        return jsonify({"access_token": token}), 200
    except Exception as e:
        logger.error(f"Error interno: {e}")
        return jsonify({"error": "Error interno en el servidor"}), 500

@app.route('/auth/logout', methods=['POST'])
@jwt_required()
@log_request
def logout():
    return jsonify({"message": "Cierre de sesión exitoso"}), 200

### Usuarios
@app.route('/usuarios/<int:id>', methods=['GET'])
@jwt_required()
@log_request
def obtener_usuario(id):
    user = servicio_usuarios.obtener_usuario_por_id(id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(user), 200

@app.route('/usuarios/<int:id>', methods=['PUT'])
@jwt_required()
@log_request
def actualizar_usuario(id):
    data = request.json
    try:
        updated_user = servicio_usuarios.actualizar_usuario(id, data)
        return jsonify({"message": "Usuario actualizado con éxito", "usuario": updated_user}), 200
    except Exception as e:
        logger.error(f"Error en /usuarios/{id}: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/usuarios/<int:id>', methods=['DELETE'])
@jwt_required()
@log_request
def eliminar_usuario(id):
    try:
        usuario = servicio_usuarios.obtener_usuario_por_id(id)
        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404
        servicio_usuarios.eliminar_usuario(id)
        return jsonify({"message": "Usuario eliminado con éxito"}), 200
    except Exception as e:
        logger.error(f"Error en /usuarios/{id}: {str(e)}")
        return jsonify({"error": "Error interno en el servidor"}), 500

@app.route('/usuarios/search', methods=['GET'])
@jwt_required()
@log_request
def buscar_usuarios():
    query = request.args.get('q', '')
    resultados = servicio_usuarios.buscar_usuarios(query)
    return jsonify(resultados), 200

# Crear un nuevo establecimiento
@app.route('/establecimientos', methods=['POST'])
@jwt_required()
@log_request
def agregar_establecimiento():
    data = request.json
    if not data or "nombre" not in data or "ubicacion" not in data:
        return jsonify({"error": "Faltan datos obligatorios"}), 400
    establecimiento = servicio_establecimientos.crear_establecimiento(data["nombre"], data["ubicacion"])
    return jsonify({"message": "Establecimiento añadido con éxito", "establecimiento": establecimiento}), 201

# Obtener un establecimiento por ID
@app.route('/establecimientos/<int:id>', methods=['GET'])
@log_request
def obtener_establecimiento(id):
    establecimiento = servicio_establecimientos.obtener_establecimiento(id)
    if not establecimiento:
        return jsonify({"error": "Establecimiento no encontrado"}), 404
    return jsonify(establecimiento), 200

# Editar un establecimiento
@app.route('/establecimientos/<int:id>', methods=['PUT'])
@jwt_required()
@log_request
def editar_establecimiento(id):
    data = request.json
    establecimiento = servicio_establecimientos.editar_establecimiento(id, data)
    if not establecimiento:
        return jsonify({"error": "Establecimiento no encontrado"}), 404
    return jsonify({"message": "Establecimiento actualizado con éxito", "establecimiento": establecimiento}), 200

# Eliminar un establecimiento
@app.route('/establecimientos/<int:id>', methods=['DELETE'])
@jwt_required()
@log_request
def eliminar_establecimiento(id):
    establecimiento = servicio_establecimientos.eliminar_establecimiento(id)
    if not establecimiento:
        return jsonify({"error": "Establecimiento no encontrado"}), 404
    return jsonify({"message": "Establecimiento eliminado con éxito"}), 200

# Buscar establecimientos
@app.route('/establecimientos/search', methods=['GET'])
@log_request
def buscar_establecimientos():
    query = request.args.get('q', '')
    resultados = servicio_establecimientos.buscar_establecimientos(query)
    return jsonify(resultados), 200

### Valoraciones
@app.route('/establecimientos/<int:id>/valoraciones', methods=['POST'])
@jwt_required()
@log_request
def agregar_valoracion(id):
    try:
        data = request.json
        if "comentario" not in data or "calificacion" not in data:
            return jsonify({"error": "Faltan datos obligatorios"}), 400
        valoracion = servicio_valoraciones.agregar_valoracion(id, data["comentario"], data["calificacion"])
        return jsonify({"message": "Valoración añadida con éxito", "valoracion": valoracion}), 201
    except KeyError as e:
        logger.error(f"Error en /establecimientos/{id}/valoraciones: {str(e)}")
        return jsonify({"error": "Error interno en el servidor"}), 500

@app.route('/establecimientos/<int:id>/valoraciones/<int:valoracion_id>', methods=['PUT'])
@jwt_required()
@log_request
def editar_valoracion(id, valoracion_id):
    try:
        data = request.json
        if "calificacion" not in data:
            return jsonify({"error": "Faltan datos obligatorios"}), 400
        valoracion = servicio_valoraciones.actualizar_valoracion(valoracion_id, data["calificacion"])
        return jsonify({"message": "Valoración actualizada con éxito", "valoracion": valoracion}), 200
    except KeyError as e:
        logger.error(f"Error en /establecimientos/{id}/valoraciones/{valoracion_id}: {str(e)}")
        return jsonify({"error": "Error interno en el servidor"}), 500

@app.route('/establecimientos/<int:id>/valoraciones/<int:valoracion_id>', methods=['DELETE'])
@jwt_required()
@log_request
def eliminar_valoracion(id, valoracion_id):
    try:
        servicio_valoraciones.eliminar_valoracion(valoracion_id)
        return jsonify({"message": "Valoración eliminada con éxito"}), 200
    except Exception as e:
        logger.error(f"Error en /establecimientos/{id}/valoraciones/{valoracion_id}: {str(e)}")
        return jsonify({"error": "Error interno en el servidor"}), 500

@app.route('/establecimientos/<int:id>/valoraciones', methods=['GET'])
@log_request
def obtener_valoraciones(id):
    valoraciones = servicio_valoraciones.obtener_valoraciones_por_establecimiento(id)
    return jsonify(valoraciones), 200

@app.route('/valoraciones/search', methods=['GET'])
@log_request
def buscar_valoraciones():
    query = request.args.get('q', '')
    resultados = servicio_valoraciones.buscar_valoraciones(query)
    return jsonify(resultados), 200

### Geolocalización
@app.route('/establecimientos/cercanos', methods=['GET'])
@log_request
def obtener_ubicaciones_cercanas():
    try:
        latitud = float(request.args.get('latitud'))
        longitud = float(request.args.get('longitud'))
        radio = float(request.args.get('radio', 5))
        ubicaciones = servicio_geolocalizacion.obtener_ubicaciones_cercanas((latitud, longitud), radio=radio)
        return jsonify(ubicaciones), 200
    except ValueError as e:
        logger.error(f"Error en /establecimientos/cercanos: {str(e)}")
        return jsonify({"error": "Parámetros inválidos"}), 400
    except Exception as e:
        logger.error(f"Error en /establecimientos/cercanos: {str(e)}")
        return jsonify({"error": "Error interno en el servidor"}), 500

if __name__ == '__main__':
    app.run(debug=True)
