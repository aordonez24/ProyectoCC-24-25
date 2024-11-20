import re
from typing import Dict


class ErrorUsuarioExistente(Exception):
    pass


class ServicioUsuarios:
    def __init__(self):
        self.usuarios = {}  # Diccionario con ID como clave
        self.current_id = 1

    def registrar_usuario(self, email, contrasena):
        if len(contrasena) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")
        if any(u["email"] == email for u in self.usuarios.values()):
            raise ErrorUsuarioExistente("El usuario ya existe.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Formato de correo no válido.")

        usuario = {"id": self.current_id, "email": email, "contrasena": contrasena}
        self.usuarios[self.current_id] = usuario
        self.current_id += 1
        return "Usuario registrado con éxito."

    def obtener_usuario(self, email):
        return next((u for u in self.usuarios.values() if u["email"] == email), None)

    def obtener_usuario_por_id(self, id_usuario):
        return self.usuarios.get(id_usuario)

    def actualizar_usuario(self, id_usuario, nuevos_datos):
        usuario = self.obtener_usuario_por_id(id_usuario)
        if not usuario:
            raise ValueError("Usuario no encontrado")
        usuario.update(nuevos_datos)
        return usuario

    def eliminar_usuario(self, id_usuario):
        usuario = self.obtener_usuario_por_id(id_usuario)
        if not usuario:
            raise ValueError("Usuario no encontrado")
        del self.usuarios[id_usuario]

    def buscar_usuarios(self, query):
        return [
            u for u in self.usuarios.values()
            if query.lower() in u["email"].lower()
        ]


# Instancia del servicio
servicio_usuarios = ServicioUsuarios()
