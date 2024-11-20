from typing import List, Dict


class ServicioValoraciones:
    """
    Servicio para gestionar valoraciones y comentarios de usuarios sobre establecimientos.
    """

    def __init__(self):
        self.valoraciones = []

    def agregar_valoracion(self, nombre_establecimiento: str, comentario: str, calificacion: int) -> Dict:
        """
        Agrega una valoración y comentario a un establecimiento.
        """
        if calificacion < 1 or calificacion > 5:
            raise ValueError("La calificación debe estar entre 1 y 5.")

        valoracion = {"establecimiento": nombre_establecimiento, "comentario": comentario, "calificacion": calificacion}
        self.valoraciones.append(valoracion)
        return valoracion

    def actualizar_valoracion(self, nombre_establecimiento: str, nueva_calificacion: int):
        for valoracion in self.valoraciones:
            if valoracion["establecimiento"] == nombre_establecimiento:
                valoracion["calificacion"] = nueva_calificacion
                return valoracion
        raise ValueError("No se encontró el establecimiento para actualizar la valoración.")

    def eliminar_valoracion(self, nombre_establecimiento: str):
        self.valoraciones = [v for v in self.valoraciones if v["establecimiento"] != nombre_establecimiento]

    def calcular_promedio_valoracion(self, nombre_establecimiento: str) -> float:
        calificaciones = [v["calificacion"] for v in self.valoraciones if
                          v["establecimiento"] == nombre_establecimiento]
        return sum(calificaciones) / len(calificaciones) if calificaciones else 0.0


# Instancia global del servicio para su reutilización
servicio_valoraciones = ServicioValoraciones()
