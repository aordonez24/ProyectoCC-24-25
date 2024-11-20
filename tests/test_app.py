import pytest
from app.app import app

@pytest.fixture
def client():
    """Configuración del cliente de prueba para Flask"""
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_headers(client):
    """Registra un usuario y obtiene un token JWT"""
    # Registro de usuario
    client.post('/auth/register', json={"email": "testuser@example.com", "nombre": "Test User", "password": "123456"})
    # Inicio de sesión
    login_response = client.post('/auth/login', json={"email": "testuser@example.com", "password": "123456"})
    assert login_response.status_code == 200, "El login falló en la generación del token"
    token = login_response.json.get("access_token")
    assert token is not None, "No se generó un token válido"
    return {"Authorization": f"Bearer {token}"}

# Tests de Autenticación
def test_register_user(client):
    response = client.post('/auth/register', json={"email": "newuser@example.com", "password": "123456"})
    print("Response JSON (Register):", response.json)  # Depuración
    assert response.status_code == 201, f"Error en /auth/register: {response.json}"
    assert "Usuario registrado con éxito" in response.json["message"], f"Unexpected message: {response.json['message']}"


def test_login_user(client):
    # Registro previo
    client.post('/auth/register', json={"email": "loginuser@example.com", "password": "123456"})
    response = client.post('/auth/login', json={"email": "loginuser@example.com", "password": "123456"})
    print("Response JSON (Login):", response.json)  # Depuración
    assert response.status_code == 200, f"Error en /auth/login: {response.json}"
    assert "access_token" in response.json


def test_logout_user(client, auth_headers):
    response = client.post('/auth/logout', headers=auth_headers)
    assert response.status_code == 200
    assert response.json["message"] == "Cierre de sesión exitoso"

# Tests de Usuarios
def test_get_user(client, auth_headers):
    response = client.get('/usuarios/1', headers=auth_headers)
    assert response.status_code == 200
    assert response.json["id"] == 1

def test_update_user(client, auth_headers):
    response = client.put('/usuarios/1', headers=auth_headers, json={"nombre": "Updated User"})
    assert response.status_code == 200
    assert response.json["message"] == "Usuario actualizado con éxito"

def test_delete_user(client, auth_headers):
    response = client.delete('/usuarios/1', headers=auth_headers)
    assert response.status_code == 200
    assert response.json["message"] == "Usuario eliminado con éxito"

# Tests de Establecimientos
def test_create_establecimiento(client, auth_headers):
    response = client.post('/establecimientos', headers=auth_headers, json={"nombre": "Restaurante X", "ubicacion": "Madrid"})
    assert response.status_code == 201
    assert response.json["message"] == "Establecimiento añadido con éxito"

def test_get_establecimiento(client, auth_headers):
    client.post('/establecimientos', headers=auth_headers, json={"nombre": "Restaurante X", "ubicacion": "Madrid"})
    response = client.get('/establecimientos/1', headers=auth_headers)
    assert response.status_code == 200
    assert response.json["nombre"] == "Restaurante X"

def test_search_establecimientos(client, auth_headers):
    client.post('/establecimientos', headers=auth_headers, json={"nombre": "Restaurante Y", "ubicacion": "Barcelona"})
    response = client.get('/establecimientos/search?q=Restaurante', headers=auth_headers)
    assert response.status_code == 200
    assert len(response.json) > 0

# Tests de Valoraciones
def test_add_valoracion(client, auth_headers):
    client.post('/establecimientos', headers=auth_headers, json={"nombre": "Restaurante Z", "ubicacion": "Sevilla"})
    response = client.post('/establecimientos/1/valoraciones', headers=auth_headers, json={"comentario": "Excelente", "calificacion": 5})
    assert response.status_code == 201
    assert response.json["message"] == "Valoración añadida con éxito"

def test_edit_valoracion(client, auth_headers):
    client.post('/establecimientos', headers=auth_headers, json={"nombre": "Restaurante Z", "ubicacion": "Sevilla"})
    client.post('/establecimientos/1/valoraciones', headers=auth_headers, json={"comentario": "Excelente", "calificacion": 5})
    response = client.put('/establecimientos/1/valoraciones/1', headers=auth_headers, json={"calificacion": 4})
    assert response.status_code == 200
    assert response.json["message"] == "Valoración actualizada con éxito"

def test_delete_valoracion(client, auth_headers):
    client.post('/establecimientos', headers=auth_headers, json={"nombre": "Restaurante Z", "ubicacion": "Sevilla"})
    client.post('/establecimientos/1/valoraciones', headers=auth_headers, json={"comentario": "Excelente", "calificacion": 5})
    response = client.delete('/establecimientos/1/valoraciones/1', headers=auth_headers)
    assert response.status_code == 200
    assert response.json["message"] == "Valoración eliminada con éxito"
