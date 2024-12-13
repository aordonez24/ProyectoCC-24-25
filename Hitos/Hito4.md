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

## Paso 2: Creación del Archivo `docker-compose.yaml`

### Justificación del Uso de `Docker Compose`

El uso de `Docker Compose` permite gestionar un conjunto de servicios que se ejecutan de manera conjunta. Esto es crucial para nuestra aplicación, ya que:

1. **Escalabilidad y Modularidad**:
   - Permite dividir la aplicación en múltiples contenedores (áreas funcionales separadas).
   - Escalar y gestionar cada contenedor de forma independiente.

2. **Reproducibilidad**:
   - Define el estado del clúster en un solo archivo `compose.yaml`.
   - Simplifica el despliegue en cualquier entorno compatible con Docker.

3. **Compatibilidad con Volúmenes**:
   - Asegura persistencia de datos mediante contenedores dedicados o volúmenes compartidos.

4. **Configuración Centralizada**:
   - Todas las configuraciones (variables de entorno, puertos, dependencias) están en un solo archivo.

### Diseño del Archivo `docker-compose.yaml`

El archivo `docker-compose.yaml` define un clúster que incluye:

- **Tres contenedores para la aplicación**:
  - Cada uno escuchando en diferentes puertos (área de balanceo y replicación).

- **Un contenedor para almacenamiento de datos**:
  - Implementado con PostgreSQL para persistencia confiable.

### Estructura del Archivo `docker-compose.yaml`

```yaml
services:
  app1:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5010:5000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://postgres:password@db/postgres
    depends_on:
      - db
    volumes:
      - logs:/app/logs

  app2:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5011:5000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://postgres:password@db/postgres
    depends_on:
      - db
    volumes:
      - logs:/app/logs

  app3:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5012:5000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://postgres:password@db/postgres
    depends_on:
      - db
    volumes:
      - logs:/app/logs

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DB: postgres
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
    driver: local
  logs:
    driver: local
```

### Explicación de la Configuración

1. **Servicios de la Aplicación (app1, app2, app3)**:
   - Construyen desde el `Dockerfile` en la raíz del proyecto.
   - Mapean puertos locales (¡5010, 5011, 5012) al puerto interno 5000.
   - Usan variables de entorno para configurar el entorno de producción y la conexión a la base de datos.
   - Comparten el volumen `logs` para almacenar registros centralizados.

2. **Servicio de Base de Datos (db)**:
   - Usa una imagen oficial de PostgreSQL.
   - Configura credenciales y nombre de la base de datos mediante variables de entorno.
   - Expone el puerto 5432 para conexión con la aplicación.
   - Utiliza un volumen `db_data` para persistir datos incluso si el contenedor se reinicia.

3. **Volúmenes**:
   - `db_data`: Persiste los datos de PostgreSQL.
   - `logs`: Centraliza los registros generados por los servicios de la aplicación.

### Comprobación

Para verificar que el archivo `docker-compose.yaml` funciona correctamente:

1. Construir y levantar el clúster:
   ```bash
   docker-compose up --build
   ```

2. Verificar que todos los servicios estén corriendo:
   ```bash
   docker ps
   ```

3. Acceder a los servicios:
   - [http://localhost:5010](http://localhost:5010)
   - [http://localhost:5011](http://localhost:5011)
   - [http://localhost:5012](http://localhost:5012)

4. Confirmar que la base de datos está accesible:
   ```bash
   psql -h localhost -U postgres -d postgres
   ```

---