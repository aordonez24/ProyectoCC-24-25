
# Hito 3: Diseño de Microservicios

## Introducción
En este hito, diseñamos un microservicio sobre la base de la funcionalidad desarrollada previamente. Este incluye:
- Una API RESTful diseñada en capas.
- Registro de actividad a través de un sistema de logs.
- Pruebas exhaustivas para verificar la funcionalidad de las rutas.
- Infraestructura adecuada para ejecutar y desplegar el microservicio.

---

## Paso 1: Justificación Técnica del Framework Elegido

### Framework Elegido: Flask

#### Razones de la Elección
1. **Ligereza y Simplicidad**:
   - Flask es un microframework que permite implementar aplicaciones web y APIs de manera rápida y eficiente.
   - Su diseño minimalista permite un control total sobre la estructura del proyecto.

2. **Extensibilidad**:
   - Tiene un ecosistema robusto de extensiones (e.g., Flask-RESTful, Flask-SQLAlchemy) que pueden integrarse según las necesidades del proyecto.

3. **Compatibilidad**:
   - Se integra fácilmente con herramientas modernas como:
     - **pytest** para la realización de pruebas.
     - **loguru** para la gestión avanzada de logs.
     - **pydantic** o **marshmallow** para validación de datos.

4. **Documentación y Comunidad**:
   - Flask cuenta con una amplia documentación y una comunidad activa, lo que facilita resolver dudas y adoptar las mejores prácticas.

5. **Ecosistema Python**:
   - Al ser compatible con otras bibliotecas de Python, permite escalar fácilmente funcionalidades avanzadas en el proyecto.

---

## Paso 2: Diseño de la API RESTful

### Descripción General
El diseño de la API se basa en un enfoque REST, donde cada ruta representa un recurso o acción específica relacionada con la funcionalidad del sistema. Las rutas están organizadas por capas para garantizar que la lógica de negocio no esté directamente acoplada a las rutas.

### Endpoints Diseñados

#### Autenticación
1. **POST /auth/register**: Registro de usuarios.
2. **POST /auth/login**: Inicio de sesión.
3. **POST /auth/logout**: Cierre de sesión.

#### Usuarios
1. **GET /usuarios/{id}**: Obtiene la información de un usuario.
2. **PUT /usuarios/{id}**: Actualiza los datos de un usuario.
3. **DELETE /usuarios/{id}**: Elimina un usuario.
4. **GET /usuarios/search**: Busca usuarios por nombre o email.

#### Establecimientos
1. **GET /establecimientos**: Devuelve una lista de establecimientos.
2. **GET /establecimientos/{id}**: Devuelve detalles de un establecimiento.
3. **POST /establecimientos**: Añade un nuevo establecimiento.
4. **PUT /establecimientos/{id}**: Edita un establecimiento.
5. **DELETE /establecimientos/{id}**: Elimina un establecimiento.
6. **GET /establecimientos/search**: Busca establecimientos por nombre o ubicación.

#### Comentarios
1. **POST /establecimientos/{id}/comentarios**: Añade un comentario a un establecimiento.
2. **PUT /establecimientos/{id}/comentarios/{comentario_id}**: Edita un comentario existente.
3. **DELETE /establecimientos/{id}/comentarios/{comentario_id}**: Elimina un comentario.
4. **GET /establecimientos/{id}/comentarios**: Devuelve los comentarios de un establecimiento.

#### Valoraciones
1. **POST /establecimientos/{id}/valoraciones**: Añade una valoración.
2. **PUT /establecimientos/{id}/valoraciones/{valoracion_id}**: Edita una valoración.
3. **DELETE /establecimientos/{id}/valoraciones/{valoracion_id}**: Elimina una valoración.
4. **GET /establecimientos/{id}/valoraciones**: Devuelve las valoraciones de un establecimiento.
5. **GET /valoraciones/search**: Busca valoraciones por puntuación o texto.

---

## Paso 3: Sistema de Logs

### Justificación Técnica
1. **Librería Elegida**: `loguru`
   - Proporciona funcionalidades avanzadas como rotación de archivos, niveles de registro y decoradores para registrar automáticamente eventos.
   - Fácil de integrar y mantener.

2. **Propósito**:
   - Registrar cada solicitud entrante con su ruta, método y tiempo de ejecución.
   - Categorizar eventos en niveles de registro: INFO, WARNING, ERROR.
   - Facilitar la depuración de errores y el análisis de uso.

### Implementación

1. **Archivo `logging_config.py`**:
   - Configura un sistema de logs con rotación de archivos (1 MB por archivo) y retención por 10 días.
   - Proporciona un decorador `log_request` para registrar solicitudes y respuestas.

2. **Integración**:
   - Todas las rutas de la API usan el decorador `@log_request` para registrar eventos automáticamente.

### Ejemplo de Salida de Logs
1. **INFO**: Solicitudes exitosas.
   ```
   2024-11-19 14:03:25.123 | INFO     | Ruta accedida: /auth/register | Método: POST
   ```

2. **WARNING**: Advertencias o situaciones anómalas.
   ```
   2024-11-19 14:08:45.912 | WARNING  | Intento de inicio de sesión fallido: malintento@example.com
   ```

3. **ERROR**: Fallos en la ejecución.
   ```
   2024-11-19 14:10:50.234 | ERROR    | Error en la ruta /usuarios/5: 'NoneType' object is not callable
   ```

---

## Próximo Paso
Escribir pruebas exhaustivas para las rutas de la API y documentar los resultados.

---

