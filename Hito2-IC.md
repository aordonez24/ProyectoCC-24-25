# Hito 2: Integración continua

## Objetivo

El principal objetivo de este hito es añadir tests y la infraestructura virtual de la aplicación, gestores de dependencias y/o tareas, necesaria para que se ejecuten los tests, además de añadir integración continua (CI) al proyecto.

## Pasos Realizados

### 1. Configuración del **gestor de tareas**
1. Se decidió utilizar **Make** como gestor de tareas por su simplicidad y estandarización.
2. Se creó un archivo `Makefile` en el directorio raíz con el siguiente contenido:

    ```Makefile
    test:
        PYTHONPATH=. pytest
    ```

   Esto define la tarea `test`, que se puede ejecutar con el comando `make test` y asegura que `pytest` se ejecute en el entorno de `PYTHONPATH` adecuado.

### 2. Elección de la **biblioteca de aserciones**
1. Se eligió **pytest** como la biblioteca de aserciones, ya que es más potente y flexible que `unittest`.
2. Se instaló pytest ejecutando el siguiente comando:

    ```bash
    pip install pytest
    ```

### 3. Elección del **test runner**
1. Se utilizó **pytest** también como test runner, ya que facilita la ejecución y el descubrimiento de pruebas.
2. Se creó un directorio `tests` donde se añadieron los archivos de prueba.
3. Ejemplo de prueba en el archivo `tests/test_app.py`:

    ```python
    def test_example():
        assert 1 + 1 == 2
    ```

4. Las pruebas se ejecutan con el comando:

    ```bash
    pytest
    ```

### 4. **Integración continua con GitHub Actions**
1. Se configuró GitHub Actions para ejecutar los tests automáticamente en cada push o pull request.
2. Se creó un archivo `.github/workflows/test.yml` 

### 5. **Implementación del archivo `pytest.ini`**
1. Se creó un archivo `pytest.ini` en el directorio raíz para definir el directorio de pruebas y establecer `PYTHONPATH`.
2. El archivo `pytest.ini` contiene la siguiente configuración:

    ```ini
    [pytest]
    testpaths = tests
    pythonpath = .
    ```

   Esto asegura que `pytest` ejecute las pruebas correctamente, encontrando todos los módulos en el proyecto sin necesidad de ajustes manuales en `PYTHONPATH`.

### 6. **Implementación de las pruebas unitarias**
1. Se identificaron aspectos principales de la lógica de negocio a testear: la geolocalización y el sistema de recomendaciones.
2. Ejemplo de prueba para la geolocalización:

    ```python
    def test_geolocation():
        location = get_nearest_location(user_coordinates)
        assert location is not None
    ```

### 7. **Justificación de las elecciones técnicas**
1. **Gestor de tareas**: Se eligió Make por su simplicidad y por ser una herramienta estándar ampliamente usada.
2. **Biblioteca de aserciones**: Se optó por pytest debido a su flexibilidad, potencia, y ecosistema robusto.
3. **Test runner**: Se eligió pytest por ser un framework de pruebas completo, que incluye su propio test runner.
4. **Integración continua**: Se configuró GitHub Actions por su integración nativa con GitHub y su facilidad de uso para automatizar las pruebas.
5. **Archivo pytest.ini**: Se incluyó este archivo para asegurar que `pytest` pueda encontrar los módulos sin problemas de rutas, lo cual es importante en la integración continua y para mejorar la consistencia en distintos entornos.
