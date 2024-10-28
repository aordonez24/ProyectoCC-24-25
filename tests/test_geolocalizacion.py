import pytest
from app.geolocalizacion import servicio_geolocalizacion


def test_obtener_ubicaciones_cercanas_radio_valido():
    ubicacion_usuario = (37.7749, -122.4194)
    radio = 5
    establecimientos = servicio_geolocalizacion.obtener_ubicaciones_cercanas(ubicacion_usuario, radio=radio)

    assert isinstance(establecimientos, list)
    assert len(establecimientos) > 0
    assert all("distancia" in est for est in establecimientos)
    assert all(est["distancia"] <= radio for est in establecimientos)


def test_obtener_ubicaciones_cercanas_radio_cero():
    ubicacion_usuario = (37.7749, -122.4194)
    with pytest.raises(ValueError):
        servicio_geolocalizacion.obtener_ubicaciones_cercanas(ubicacion_usuario, radio=0)


def test_calcular_distancia_ubicacion_invalida():
    with pytest.raises(ValueError):
        servicio_geolocalizacion.calcular_distancia("invalido", (37.7749, -122.4194))


def test_obtener_ubicaciones_sin_resultados():
    ubicacion_usuario = (0, 0)
    radio = 5
    establecimientos = servicio_geolocalizacion.obtener_ubicaciones_cercanas(ubicacion_usuario, radio=radio)
    assert establecimientos == []
