import pytest
from app.services.establecimiento import ServicioEstablecimientos

@pytest.fixture
def servicio():
    """Instancia el servicio de establecimientos para cada test."""
    return ServicioEstablecimientos()

def test_crear_establecimiento(servicio):
    establecimiento = servicio.crear_establecimiento("Restaurante A", "Madrid")
    assert establecimiento["id"] == 1
    assert establecimiento["nombre"] == "Restaurante A"
    assert establecimiento["ubicacion"] == "Madrid"
    assert len(servicio.establecimientos) == 1

def test_obtener_establecimiento(servicio):
    servicio.crear_establecimiento("Restaurante B", "Barcelona")
    establecimiento = servicio.obtener_establecimiento(1)
    assert establecimiento is not None
    assert establecimiento["id"] == 1
    assert establecimiento["nombre"] == "Restaurante B"
    assert establecimiento["ubicacion"] == "Barcelona"

def test_obtener_establecimiento_no_existente(servicio):
    establecimiento = servicio.obtener_establecimiento(999)
    assert establecimiento is None

def test_editar_establecimiento(servicio):
    servicio.crear_establecimiento("Restaurante C", "Sevilla")
    establecimiento_actualizado = servicio.editar_establecimiento(1, {"ubicacion": "Malaga"})
    assert establecimiento_actualizado is not None
    assert establecimiento_actualizado["ubicacion"] == "Malaga"

def test_editar_establecimiento_no_existente(servicio):
    establecimiento_actualizado = servicio.editar_establecimiento(999, {"ubicacion": "Valencia"})
    assert establecimiento_actualizado is None

def test_eliminar_establecimiento(servicio):
    servicio.crear_establecimiento("Restaurante D", "Bilbao")
    eliminado = servicio.eliminar_establecimiento(1)
    assert eliminado is not None
    assert eliminado["id"] == 1
    assert len(servicio.establecimientos) == 0

def test_eliminar_establecimiento_no_existente(servicio):
    eliminado = servicio.eliminar_establecimiento(999)
    assert eliminado is None

def test_buscar_establecimientos(servicio):
    servicio.crear_establecimiento("Restaurante E", "Madrid")
    servicio.crear_establecimiento("Cafetería F", "Madrid")
    resultados = servicio.buscar_establecimientos("Restaurante")
    assert len(resultados) == 1
    assert resultados[0]["nombre"] == "Restaurante E"

def test_buscar_establecimientos_sin_coincidencias(servicio):
    servicio.crear_establecimiento("Restaurante G", "Barcelona")
    resultados = servicio.buscar_establecimientos("Pizzería")
    assert len(resultados) == 0
