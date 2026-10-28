### BarinasRoute - Plataforma de Gestión de Movilidad Urbana

**Asignatura:** Desarrollo de Aplicaciones I  

**Estudiante:** Edgarlyn Parra 

**Sección:** FS-01

**Profesor:** Rafael Barrios  

---

### Metodología de Desarrollo en V (Ciclo de Vida y Estrategia de Pruebas)

La metodología en V es un modelo de desarrollo secuencial donde cada fase de diseño y especificación (rama descendente) se corresponde directamente con un nivel de pruebas (rama ascendente), teniendo a la codificación como el punto de inflexión.

```markdown


```text
[ Análisis de Requisitos ]  ---------------------------->  [ Pruebas de Aceptación ]
          \                                                               /
   [ Análisis del Sistema ]  --------------------------->  [ Pruebas de Sistema ]
             \                                                           /
      [ Diseño de Software ]  -------------------------->  [ Pruebas de Integración ]
                \                                                        /
         [ Diseño de Módulos ]  ------------------------>  [ Pruebas Unitarias ]
                   \                                                    /
                    -------------> [ CODIFICACIÓN ] <-----

```
### 1. Análisis de Requisitos (Requirement Gathering)

Esta etapa inicial se enfoca en recopilar, analizar y formalizar las necesidades operativas de los usuarios y las reglas de negocio del sistema, generando especificaciones funcionales, historias de usuario y matrices de trazabilidad. En BarinasRoute, esta fase consistió en identificar las fallas de información en el transporte urbano de Barinas, abordando la desorientación provocada por variantes de ruta no señalizadas (como la bifurcación entre Letra A y Letra B), el uso de paradas basadas en toponimia popular sin georreferenciación y la falta de canales directos para reportar incidentes viales. Su fase de validación vinculada corresponde a las Pruebas de Aceptación, las cuales comprueban que el software resuelva los problemas cotidianos de traslado de la ciudadanía.

### 2. Análisis del Sistema (System Analysis)

En esta fase se transforman los requerimientos del usuario en especificaciones técnicas formales, delimitando las fronteras del software, los flujos de interacción y las responsabilidades operativas mediante casos de uso y diagramas de flujo de datos. En el contexto de BarinasRoute, se establecieron los límites funcionales de la plataforma y el modelo de control de acceso basado en roles (RBAC), definiendo las capacidades de navegación libre para Visitantes, reporte de incidencias para Usuarios Ciudadanos, moderación de alertas viales para Gestores y administración de líneas de transporte para Administradores. Su fase de verificación asociada son las Pruebas del Sistema, encargadas de evaluar el comportamiento global e integral de la plataforma de extremo a extremo.

### 3. Diseño de Software / Arquitectura (Software Design)

Esta fase define la infraestructura estructural del proyecto, organizando la solución en capas desacopladas, estableciendo los mecanismos de persistencia y seleccionando el stack tecnológico adecuado para el despliegue. Para BarinasRoute, se diseñó una arquitectura web modular con backend en Python y Django 4.2 LTS, un entorno de empaquetado y compilación frontend con Vite.js acoplado a interfaces en Bootstrap 5, un visor cartográfico basado en Leaflet.js sobre OpenStreetMap y la contenedorización de todos los servicios mediante Docker y Docker Compose. Se vincula de forma directa con las Pruebas de Integración, cuyo propósito es certificar que la comunicación entre las capas de presentación, lógica de servidor, empaquetador de assets y base de datos opere de manera coordinada.

### 4. Diseño de Módulos (Module Design)

Esta etapa aborda la especificación técnica de bajo nivel para cada componente interno, formalizando la lógica de negocio, los algoritmos de procesamiento y los modelos de datos de las aplicaciones del proyecto. En BarinasRoute, esto se materializó en el diseño relacional de entidades en `models.py` para líneas, variantes, paradas y reportes de incidentes, la codificación de vistas y controladores en `views.py`, los formularios de validación y autenticación en `forms.py`, el enrutamiento interno en `urls.py` y los algoritmos de proximidad geográfica para el cálculo de paradas cercanas. Su contraparte de control son las Pruebas Unitarias, orientadas a validar que cada método, función y regla de validación responda de forma exacta y aislada.

### Punto de Inflexión: Codificación (Coding)

Representa la etapa donde las especificaciones técnicas y los diseños previos se materializan en código fuente ejecutable, aplicando estándares limpios de desarrollo y entornos reproducibles. En BarinasRoute, la codificación se llevó a cabo integrando los módulos de Django con la compilación de scripts en Vite.js, ejecutando el aplicativo dentro de contenedores aislados de Docker y manteniendo el versionado continuo del código mediante Git y GitHub.

```
---
S

 **1. Clonar el repositorio:**

```bash
git clone [https://github.com/Joiset/proyecto_web_JOI.git](https://github.com/Joiset/proyecto_web_JOI.git)
cd proyecto_web_JOI

```

**2. Construir la imagen del proyecto:**

```bash
docker compose build

```

**3. Ejecutar migraciones de la base de datos:**

```bash
docker compose run --rm web python manage.py migrate

```

**4. Crear usuario administrador:**

```bash
docker compose run --rm web python manage.py createsuperuser

```

**5. Iniciar el servidor:**

```bash
docker compose up

```

**disponible en el navegador:** 

```bash
 http://localhost:8000

```


