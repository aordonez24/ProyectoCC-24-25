from typing import List, Dict


class ServicioRecomendaciones:
    """
    Servicio para proporcionar recomendaciones de establecimientos según las preferencias del usuario.
    """

    def __init__(self):
        self.establecimientos = [
            {"nombre": "Restaurante A", "sin_gluten": True, "al_aire_libre": True, "valoracion": 4.5},
            {"nombre": "Cafetería B", "sin_gluten": False, "al_aire_libre": True, "valoracion": 3.5},
            {"nombre": "Panadería C", "sin_gluten": True, "al_aire_libre": False, "valoracion": 4.0},
        ]

    def obtener_recomendaciones(self, preferencias_usuario: Dict, valoracion_minima: float = 0) -> List[Dict]:
        """
        Filtra los establecimientos según las preferencias y la valoración mínima.

        Parámetros:
        - preferencias_usuario: Diccionario con preferencias de usuario (ej. sin_gluten, al_aire_libre).
        - valoracion_minima: Valoración mínima deseada.

        Retorna:
        - Lista de establecimientos ordenados por valoración.
        """
        if not isinstance(preferencias_usuario, dict):
            raise ValueError("Las preferencias del usuario deben ser un diccionario.")

        establecimientos_filtrados = [
            est for est in self.establecimientos
            if all(preferencias_usuario.get(clave, est[clave]) == est[clave] for clave in preferencias_usuario)
               and est["valoracion"] >= valoracion_minima
        ]

        return sorted(establecimientos_filtrados, key=lambda x: x["valoracion"], reverse=True)

    def buscar_establecimientos(self, query: str):
        return [e for e in self.establecimientos if query.lower() in e["nombre"].lower()]


# Instancia global del servicio para su reutilización
servicio_recomendaciones = ServicioRecomendaciones()
