import pytest
from app.services.usuario import ServicioUsuarios, ErrorUsuarioExistente

servicio = ServicioUsuarios()

def test_registro_usuario_correo_invalido():
    with pytest.raises(ValueError, match="Formato de correo no válido."):
        servicio.registrar_usuario("correo_invalido", "123456")


def test_registro_usuario_contrasena_corta():
    with pytest.raises(ValueError, match="La contraseña debe tener al menos 6 caracteres."):
        servicio.registrar_usuario("test@example.com", "123")

def test_registro_usuario_existente():
    servicio.registrar_usuario("existente@example.com", "123456")
    with pytest.raises(ErrorUsuarioExistente):
        servicio.registrar_usuario("existente@example.com", "123456")
