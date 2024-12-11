# Hito 4: Composición de Servicios

## Paso 1: Creación del Dockerfile

### Justificación del Dockerfile

El `Dockerfile` es el archivo base para construir una imagen de Docker que contendrá nuestra aplicación. Es esencial para garantizar que nuestra aplicación sea ejecutable en cualquier entorno que soporte Docker. La elección de los componentes del Dockerfile está basada en los siguientes criterios:

1. **Elección del contenedor base**:
   - Usamos `python:3.12-slim` como base debido a:
     - Su ligereza, lo que reduce el tamaño de la imagen.
     - La disponibilidad de Python 3.12, compatible con la aplicación.
     - Proporciona flexibilidad para instalar dependencias adicionales.

2. **Instalación de paquetes adicionales**:
   - Se instalarán las dependencias necesarias listadas en `requirements.txt` para garantizar el funcionamiento correcto de la aplicación.
   - Se incluye `gunicorn` para servir la aplicación Flask en un entorno de producción.

3. **Copiado del código fuente**:
   - La estructura del proyecto se respeta al copiar los directorios relevantes al contenedor.

4. **Exposición de puertos**:
   - Se expone el puerto `5000` para que la aplicación sea accesible externamente.

5. **Comando de ejecución**:
   - La aplicación se inicia usando `gunicorn` para manejar múltiples workers y garantizar un rendimiento estable.

### Ubicación del Dockerfile

El `Dockerfile` se ha colocado en la **raíz del proyecto**. Esto facilita la configuración y permite que Docker acceda fácilmente a los archivos necesarios como `requirements.txt` y al código fuente de la aplicación.

La estructura del proyecto ahora luce así:
```
OcioSinGluten/
├── .github/
├── .venv/
├── app/
├── Hitos/
├── logs/
├── static/
├── templates/
├── tests/
├── utils/
├── .gitignore
├── DOCUMENTACION.md
├── INFORMACION.md
├── LICENSE
├── Makefile
├── pytest.ini
├── README.md
├── requirements.txt
├── Dockerfile
```

### Comprobación
Para verificar que el `Dockerfile` funciona correctamente:

1. Construir la imagen de Docker:
   ```bash
   docker build -t ocio-sin-gluten .
   ```

2. Ejecutar el contenedor:
   ```bash
   docker run -p 5000:5000 ocio-sin-gluten
   ```

3. Acceder a la aplicación en [http://localhost:5000](http://localhost:5000).

4. Confirmar que todos los endpoints están funcionales.

---

En el siguiente paso, configuraremos el archivo `compose.yaml` para crear un clúster con múltiples contenedores.