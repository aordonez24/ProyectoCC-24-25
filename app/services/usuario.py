import re
from typing import Dict


class ErrorUsuarioExistente(Exception):
    pass


class ServicioUsuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, email, contrasena):
        if email in self.usuarios:
            raise ValueError("El usuario ya existe.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Correo inválido.")
        if len(contrasena) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")
        self.usuarios[email] = {"email": email, "contrasena": contrasena}
        return "Usuario registrado con éxito."

    def obtener_usuario(self, email):
        return self.usuarios.get(email)

    def obtener_usuario_por_id(self, id_usuario):
        # Simula una base de datos con IDs
        usuarios_list = list(self.usuarios.values())
        if id_usuario > len(usuarios_list) or id_usuario < 1:
            return None
        return {"id": id_usuario, **usuarios_list[id_usuario - 1]}

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
        del self.usuarios[usuario["correo"]]

    def buscar_usuarios(self, query):
        return [u for u in self.usuarios.values() if query.lower() in u["correo"].lower()]

servicio_usuarios = ServicioUsuarios()
