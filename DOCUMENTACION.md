# Documentación del Proyecto - OcioSinGluten

## Introducción

Este archivo contiene información sobre la realización y desarrollo del proyecto **OcioSinGluten**, una red social para personas con celiaquía, que les permite descubrir y compartir establecimientos que ofrecen opciones sin gluten. El backend está siendo migrado de **Java** a **Python**, utilizando tecnologías modernas para mejorar la eficiencia y escalabilidad de la aplicación.

## Objetivos

Los principales objetivos de este documento son:

- **Documentar el proceso de desarrollo**: Registrar decisiones técnicas y cambios importantes durante el desarrollo.
- **Explicar la arquitectura del proyecto**: Describir cómo se estructuran las distintas partes del proyecto.
- **Mantener un registro de futuras funcionalidades**: Enumerar características que serán implementadas más adelante.
- **Facilitar la contribución de otros desarrolladores**: Proveer una guía clara para que nuevos colaboradores puedan integrarse fácilmente al proyecto.

## Decisiones Técnicas

### Migración de Java a Python

- El backend original fue desarrollado en **Java** durante mi Trabajo de Fin de Grado (TFG). Sin embargo, he decidido migrar el backend a **Python**, utilizando frameworks como **Django** o **Flask**, debido a las siguientes ventajas:
  - Mayor simplicidad y rapidez en el desarrollo.
  - Una comunidad de desarrolladores más extensa y recursos más accesibles.
  - Mejor soporte para integración continua y despliegue en la nube.

### Arquitectura Inicial del Proyecto

- **Frontend**: Se planea utilizar **React.js** o **Vue.js** (por definir) para el desarrollo de la interfaz de usuario.
- **Backend**: El backend estará basado en **Python** con **Django** o **Flask**, según las necesidades del proyecto.
- **Base de Datos**: Aún por determinar.
- **Servicios en la nube**: Aún por determinar.
- **CI/CD**: Integración continua a través de **GitHub Actions** para asegurar que el código nuevo sea probado automáticamente.

## Próximos Pasos

- **Creación del entorno de desarrollo** para comenzar con la redacción del código.
- **Definir el framework final** para el backend (entre Django y Flask).
- **Diseñar la base de datos** que manejará la información de usuarios y establecimientos.
- **Implementar las pruebas unitarias** para asegurar la calidad del código.
- **Crear la funcionalidad de registro de usuarios** con autenticación segura.
  
## Funcionalidades Futuras

1. **Sistema de Recomendaciones**: Implementar un sistema que sugiera establecimientos basados en las preferencias y valoraciones de los usuarios.
2. **Geolocalización**: Mostrar en tiempo real los establecimientos sin gluten cercanos al usuario.
3. **Chat entre Usuarios**: Agregar un chat interno para que los usuarios puedan intercambiar opiniones y recomendaciones.

## Actualizaciones del Proyecto

Este documento será actualizado conforme avance el desarrollo de **OcioSinGluten**. Cada hito del proyecto incluirá una actualización en este archivo para reflejar los cambios y decisiones tomadas durante el desarrollo.

## Contribuciones

Si deseas contribuir al proyecto, por favor revisa el archivo [INFORMACION](./INFORMACION.md) para conocer las instrucciones de contribución y las buenas prácticas recomendadas.


**Fecha de última actualización**: 30 de Septiembre de 2024
