import pytest
from app.recomendaciones import servicio_recomendaciones


def test_obtener_recomendaciones_preferencias_usuario():
    preferencias_usuario = {"sin_gluten": True}
    recomendaciones = servicio_recomendaciones.obtener_recomendaciones(preferencias_usuario)

    assert isinstance(recomendaciones, list)
    assert len(recomendaciones) > 0
    assert all(rec["sin_gluten"] == preferencias_usuario["sin_gluten"] for rec in recomendaciones)


def test_obtener_recomendaciones_valoracion_minima():
    preferencias_usuario = {"sin_gluten": True}
    recomendaciones = servicio_recomendaciones.obtener_recomendaciones(preferencias_usuario, valoracion_minima=4.5)

    assert len(recomendaciones) == 1
    assert recomendaciones[0]["nombre"] == "Restaurante A"
    assert recomendaciones[0]["valoracion"] >= 4.5


def test_obtener_recomendaciones_ordenado_por_valoracion():
    preferencias_usuario = {"al_aire_libre": True}
    recomendaciones = servicio_recomendaciones.obtener_recomendaciones(preferencias_usuario)

    valoraciones = [rec["valoracion"] for rec in recomendaciones]
    assert valoraciones == sorted(valoraciones, reverse=True)


def test_obtener_recomendaciones_con_preferencia_invalida():
    with pytest.raises(ValueError):
        servicio_recomendaciones.obtener_recomendaciones("preferencia_invalida")
