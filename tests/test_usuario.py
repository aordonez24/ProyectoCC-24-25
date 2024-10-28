import pytest
from app.usuario import servicio_usuarios, ErrorUsuarioExistente

def test_registro_usuario_exitoso():
    resultado = servicio_usuarios.registrar_usuario("usuario_unico@example.com", "contrasenaSegura123")
    assert resultado == "Usuario creado exitosamente"

def test_registro_usuario_correo_duplicado():
    servicio_usuarios.registrar_usuario("usuario_duplicado@example.com", "contrasenaSegura123")
    with pytest.raises(ErrorUsuarioExistente):
        servicio_usuarios.registrar_usuario("usuario_duplicado@example.com", "otraContrasena")

def test_registro_usuario_correo_invalido():
    with pytest.raises(ValueError):
        servicio_usuarios.registrar_usuario("correo_invalido", "contrasenaSegura123")

def test_registro_usuario_contrasena_corta():
    with pytest.raises(ValueError):
        servicio_usuarios.registrar_usuario("usuario_nuevo@example.com", "123")
