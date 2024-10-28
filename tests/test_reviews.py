import pytest
from app.valoracion import servicio_valoraciones

def test_agregar_valoracion_exitosa():
    valoracion = servicio_valoraciones.agregar_valoracion("Restaurante Prueba", "Excelente!", 5)
    assert valoracion["comentario"] == "Excelente!"
    assert valoracion["calificacion"] == 5
    assert valoracion["establecimiento"] == "Restaurante Prueba"

def test_agregar_valoracion_calificacion_invalida():
    with pytest.raises(ValueError):
        servicio_valoraciones.agregar_valoracion("Restaurante Prueba", "Muy malo", 0)

def test_actualizar_valoracion_exitosa():
    servicio_valoraciones.agregar_valoracion("Restaurante Actualizado", "Muy bueno", 4)
    valoracion_actualizada = servicio_valoraciones.actualizar_valoracion("Restaurante Actualizado", 5)
    assert valoracion_actualizada["calificacion"] == 5

def test_actualizar_valoracion_no_existente():
    with pytest.raises(ValueError):
        servicio_valoraciones.actualizar_valoracion("Restaurante Inexistente", 3)

def test_eliminar_valoracion():
    servicio_valoraciones.agregar_valoracion("Restaurante a Eliminar", "Excelente!", 5)
    servicio_valoraciones.eliminar_valoracion("Restaurante a Eliminar")
    promedio = servicio_valoraciones.calcular_promedio_valoracion("Restaurante a Eliminar")
    assert promedio == 0.0

def test_calcular_promedio_valoracion():
    servicio_valoraciones.agregar_valoracion("Restaurante Valorado", "Muy bueno", 4)
    servicio_valoraciones.agregar_valoracion("Restaurante Valorado", "Excelente", 5)
    promedio = servicio_valoraciones.calcular_promedio_valoracion("Restaurante Valorado")
    assert promedio == pytest.approx(4.5, 0.1)
