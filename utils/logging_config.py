from functools import wraps
from flask import request
from loguru import logger

logger.add("logs/api.log", rotation="1 MB", retention="10 days", level="INFO")

def log_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Ruta accedida: {request.path} | Método: {request.method}")
        try:
            response = func(*args, **kwargs)
            if isinstance(response, tuple):  # Verificar si la respuesta es un tuple
                response_obj, status_code = response
                logger.info(f"Respuesta: {status_code}")
                return response
            logger.info(f"Respuesta: {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"Error en la ruta {request.path}: {str(e)}")
            raise
    return wrapper

