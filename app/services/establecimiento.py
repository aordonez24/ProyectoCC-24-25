class ServicioEstablecimientos:
    def __init__(self):
        self.establecimientos = []
        self.current_id = 1

    def crear_establecimiento(self, nombre, ubicacion):
        establecimiento = {
            "id": self.current_id,
            "nombre": nombre,
            "ubicacion": ubicacion,
        }
        self.establecimientos.append(establecimiento)
        self.current_id += 1
        return establecimiento

    def obtener_establecimiento(self, id):
        return next((e for e in self.establecimientos if e["id"] == id), None)

    def editar_establecimiento(self, id, data):
        establecimiento = self.obtener_establecimiento(id)
        if not establecimiento:
            return None
        establecimiento.update(data)
        return establecimiento

    def eliminar_establecimiento(self, id):
        establecimiento = self.obtener_establecimiento(id)
        if establecimiento:
            self.establecimientos.remove(establecimiento)
        return establecimiento

    def buscar_establecimientos(self, query):
        return [
            e for e in self.establecimientos if query.lower() in e["nombre"].lower()
        ]


# Instancia del servicio
servicio_establecimientos = ServicioEstablecimientos()
