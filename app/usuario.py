import re
from typing import Dict


class ErrorUsuarioExistente(Exception):
    pass


class ServicioUsuarios:
    """
    Servicio para el manejo de usuarios, incluyendo registro y autenticación básica.
    """

    def __init__(self):
        self.usuarios = {}

    def validar_correo(self, correo: str) -> bool:
        """ Valida el formato de un correo electrónico. """
        return re.match(r"[^@]+@[^@]+\.[^@]+", correo) is not None

    def registrar_usuario(self, correo: str, contrasena: str) -> str:
        """
        Registra un usuario, validando formato de correo y evitando duplicados.

        Parámetros:
        - correo: Correo electrónico del usuario.
        - contrasena: Contraseña del usuario.

        Retorna:
        - Mensaje de éxito o lanza excepción en caso de error.
        """
        if not self.validar_correo(correo):
            raise ValueError("Formato de correo no válido.")
        if len(contrasena) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")
        if correo in self.usuarios:
            raise ErrorUsuarioExistente(f"El usuario con correo {correo} ya existe.")

        self.usuarios[correo] = {"correo": correo, "contrasena": contrasena}
        return "Usuario creado exitosamente"


# Instancia global del servicio para su reutilización
servicio_usuarios = ServicioUsuarios()
