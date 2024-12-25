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

