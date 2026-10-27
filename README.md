# Proyecto Web - Desarrollo de Aplicaciones I

## Metodología de Desarrollo en V (Fase Descendente / Verificación)

La metodología en V es un modelo de desarrollo secuencial donde cada fase de diseño y especificación (rama descendente) se corresponde directamente con un nivel de pruebas (rama ascendente), teniendo a la codificación como el punto de inflexión.

[ Análisis de Requisitos ]  ------------------>  [ Pruebas de Aceptación ]
\                                            /
[ Análisis del Sistema ]  ------------------>  [ Pruebas de Sistema ]
\                                        /
[ Diseño de Software / Arquitectura ]  --->  [ Pruebas de Integración ]
\                                    /
[ Diseño de Módulos ]  ----------->  [ Pruebas Unitarias ]
\                            /
-----> [ CODIFICACIÓN ] <---

### 1. Análisis de Requisitos (Requirement Gathering)
* **Definición:** Es la fase inicial donde se recopilan, analizan y documentan las necesidades del usuario final y las reglas del negocio.
* **Entregables:** Documento de Especificación de Requisitos de Software (SRS), historias de usuario y matriz de trazabilidad.
* **Fase de prueba asociada:** Pruebas de Aceptación (validan que el sistema resuelva el problema real del usuario).

### 2. Análisis del Sistema (System Analysis)
* **Definición:** Traducción de las necesidades del usuario en especificaciones técnicas y funcionales del sistema. Se definen las interfaces de entrada/salida y los límites de la aplicación.
* **Entregables:** Casos de uso, diagramas de flujo de datos y especificaciones de comportamiento general del software.
* **Fase de prueba asociada:** Pruebas del Sistema (validan la funcionalidad completa de extremo a extremo).

### 3. Diseño de Software / Arquitectura (Software Design)
* **Definición:** Se establece la estructura tecnológica general del software, la relación entre capas (frontend, backend, base de datos) y la infraestructura de despliegue.
* **Entregables:** Diagrama de componentes, definición del stack tecnológico (Python, Django, Vite.js, Docker y base de datos relacional) y protocolos de comunicación e interfaces.
* **Fase de prueba asociada:** Pruebas de Integración (comprueban la comunicación fluida entre módulos y servicios externos).

### 4. Diseño de Módulos (Module Design)
* **Definición:** Especificación detallada de bajo nivel de cada componente individual del sistema (lógica interna, algoritmos y estructuras de almacenamiento).
* **Entregables:** Esquemas de bases de datos (`models.py`), lógica de control (`views.py`), validaciones (`forms.py`) y mapeo de rutas (`urls.py`).
* **Fase de prueba asociada:** Pruebas Unitarias (validan funciones, clases y métodos de forma aislada).

### Punto de Inflexión: Codificación (Coding)
* Es la fase donde se traduce todo el diseño previo a código fuente ejecutable, aplicando buenas prácticas de programación, control de versiones y entornos de desarrollo aislados.
