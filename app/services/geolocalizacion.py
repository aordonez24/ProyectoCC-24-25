import math
from typing import List, Tuple, Dict


class ServicioGeolocalizacion:
    """
    Servicio para obtener establecimientos cercanos en función de la ubicación del usuario.
    Proporciona métodos para calcular distancias y filtrar establecimientos en un radio específico.
    """

    def __init__(self):
        # Lista simulada de establecimientos con ubicaciones.
        self.establecimientos = [
            {"nombre": "Restaurante A", "ubicacion": (37.7749, -122.4194)},
            {"nombre": "Cafetería B", "ubicacion": (37.7849, -122.4094)},
            {"nombre": "Panadería C", "ubicacion": (37.7949, -122.4294)},
        ]

    def calcular_distancia(self, loc1: Tuple[float, float], loc2: Tuple[float, float]) -> float:
        """
        Calcula la distancia euclidiana entre dos puntos de coordenadas (latitud, longitud).
        """
        if not isinstance(loc1, tuple) or not isinstance(loc2, tuple) or len(loc1) != 2 or len(loc2) != 2:
            raise ValueError("Las ubicaciones deben ser tuplas de coordenadas válidas (latitud, longitud).")

        return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

    def obtener_ubicaciones_cercanas(self, ubicacion_usuario: Tuple[float, float], radio: float) -> List[Dict]:
        """
        Retorna los establecimientos dentro del radio especificado desde la ubicación del usuario.

        Parámetros:
        - ubicacion_usuario: Tupla (latitud, longitud) del usuario.
        - radio: Radio en kilómetros.

        Retorna:
        - Lista de diccionarios con establecimientos dentro del radio.
        """
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero.")

        ubicaciones_filtradas = []
        for establecimiento in self.establecimientos:
            distancia = self.calcular_distancia(ubicacion_usuario, establecimiento["ubicacion"])
            if distancia <= radio:
                ubicaciones_filtradas.append({**establecimiento, "distancia": distancia})

        return sorted(ubicaciones_filtradas, key=lambda x: x["distancia"])


# Instancia global del servicio para su reutilización
servicio_geolocalizacion = ServicioGeolocalizacion()
