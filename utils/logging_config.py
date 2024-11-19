from loguru import logger
from flask import request

# Configuración básica del logger
logger.add("logs/api.log", rotation="1 MB", retention="10 days", level="INFO")

def log_request(func):
    """
    Decorador para registrar cada solicitud entrante.
    """
    def wrapper(*args, **kwargs):
        logger.info(f"Ruta accedida: {request.path} | Método: {request.method}")
        try:
            response = func(*args, **kwargs)
            logger.info(f"Respuesta: {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"Error en la ruta {request.path}: {e}")
            raise
    return wrapper
