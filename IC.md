#  Hito 2: Integración continua

## Objetivo

El principal objetivo de este hito es añadir tests y la infraestructura virtual de la aplicación, gestores de dependencias y/o tareas, necesaria para que se ejecuten los tests, además de añadir integración continua (CI) al proyecto.

## Pasos Realizados

### 1. Configuración del **gestor de tareas**
1. Se decidió utilizar **Make** como gestor de tareas por su simplicidad y estandarización.
2. Se creó un archivo `Makefile` en el directorio raíz con el siguiente contenido:

    ```Makefile
    test:
        pytest
    ```

   Esto define la tarea `test`, que se puede ejecutar con el comando `make test`.

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
2. Se creó un archivo `.github/workflows/test.yml` con el siguiente contenido:

    ```yaml
    name: Run Tests

    on: [push, pull_request]

    jobs:
      test:
        runs-on: ubuntu-latest
        
        steps:
        - name: Checkout code
          uses: actions/checkout@v2

        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: '3.x'

        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install pytest

        - name: Run tests
          run: pytest
    ```

### 5. **Implementación de las pruebas unitarias**
1. Se identificaron aspectos principales de la lógica de negocio a testear: la geolocalización y el sistema de recomendaciones.
2. Ejemplo de prueba para la geolocalización:

    ```python
    def test_geolocation():
        location = get_nearest_location(user_coordinates)
        assert location is not None
    ```

### 6. **Justificación de las elecciones técnicas**
1. **Gestor de tareas**: Se eligió Make por su simplicidad y por ser una herramienta estándar ampliamente usada.
2. **Biblioteca de aserciones**: Se optó por pytest debido a su flexibilidad, potencia, y ecosistema robusto.
3. **Test runner**: Se eligió pytest por ser un framework de pruebas completo, que incluye su propio test runner.
4. **Integración continua**: Se configuró GitHub Actions por su integración nativa con GitHub y su facilidad de uso para automatizar las pruebas.