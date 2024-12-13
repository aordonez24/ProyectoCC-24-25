import pytest
import requests

# Direcciones y puertos de las aplicaciones
APPS = [
    {"name": "app1", "url": "http://localhost:5010"},
    {"name": "app2", "url": "http://localhost:5011"},
    {"name": "app3", "url": "http://localhost:5012"}
]

# Base URL para la base de datos (PostgreSQL)
DATABASE_URL = "http://localhost:5432"

@pytest.mark.parametrize("app", APPS)
def test_app_health(app):
    """Verificar que cada instancia de la aplicación responde correctamente."""
    response = requests.get(f"{app['url']}/health")
    assert response.status_code == 200, f"{app['name']} no está disponible."
    assert response.json().get("status") == "ok", f"{app['name']} no responde correctamente."

@pytest.mark.parametrize("app", APPS)
def test_database_connection(app):
    """Verificar que las aplicaciones pueden conectarse a la base de datos."""
    # Intentar realizar una operación básica en la base de datos desde la aplicación
    response = requests.post(
        f"{app['url']}/test-db",
        json={"query": "SELECT 1;"}
    )
    assert response.status_code == 200, f"{app['name']} no puede conectar con la base de datos."
    assert response.json().get("result") == 1, f"{app['name']} no puede realizar consultas en la base de datos."

@pytest.mark.parametrize("app", APPS)
def test_persistence(app):
    """Verificar que los datos persisten después de reiniciar el clúster."""
    # Insertar un dato
    insert_response = requests.post(
        f"{app['url']}/data",
        json={"key": "test_key", "value": "test_value"}
    )
    assert insert_response.status_code == 201, f"No se pudo insertar datos en {app['name']}."

    # Reiniciar el clúster
    import os
    os.system("docker-compose restart")

    # Verificar que los datos persisten
    retrieve_response = requests.get(f"{app['url']}/data/test_key")
    assert retrieve_response.status_code == 200, f"Los datos no persisten en {app['name']}."
    assert retrieve_response.json().get("value") == "test_value", f"Valor incorrecto en {app['name']}."

