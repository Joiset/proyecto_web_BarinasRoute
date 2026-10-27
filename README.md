### BarinasRoute - Plataforma de Gestión de Movilidad Urbana

**Asignatura:** Desarrollo de Aplicaciones I  

**Estudiante:** Edgarlyn Parra 

**Sección:** FS-01

**Profesor:** Alex Barrios  

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
Fase inicial donde se identificaron las necesidades del usuario y la dinámica del transporte público en Barinas (rutas, desvíos y tarifas). Se documentan los requerimientos funcionales, historias de usuario y la matriz de trazabilidad. Su fase de prueba asociada son las Pruebas de Aceptación, encargadas de confirmar que el sistema resuelva los problemas reales de movilidad.


### 2. Análisis del Sistema (System Analysis)
Traducción de los requisitos del usuario a especificaciones técnicas y operativas del software, definiendo límites del sistema, casos de uso y diagramas de flujo. Se vincula con las Pruebas del Sistema, las cuales validan el comportamiento global de la aplicación de extremo a extremo.


### 3. Diseño de Software / Arquitectura (Software Design)
Definición de la arquitectura tecnológica general: estructura modular desacoplada en Django, persistencia en base de datos relacional y contenedorización de servicios con Docker. Se asocia con las Pruebas de Integración, destinadas a comprobar la comunicación correcta entre los módulos del sistema y servicios externos.


### 4. Diseño de Módulos (Module Design)
Especificación de bajo nivel de cada componente individual: definición de tablas y esquemas relacionales (models.py), lógica de control (views.py), validación de entradas (forms.py) y mapeo de endpoints (urls.py). Su fase de prueba correspondiente son las Pruebas Unitarias, verificando que las funciones y métodos operen correctamente de forma aislada.


### 5. Punto de Inflexión: Codificación (Coding)
Etapa de implementación técnica donde se construyen los módulos en código Python/Django sobre Docker, aplicando estándares limpios de desarrollo y control de versiones con Git.


### 6. Pruebas Unitarias (Unit Testing)
Primera fase de verificación tras la codificación. Evalúa de forma aislada la lógica de los métodos de modelos, la asignación automática de perfiles por señales y las validaciones de formularios.


### 7. Pruebas de Integración (Integration Testing)
Comprueba el trabajo conjunto entre módulos: valida que el control de acceso por roles proteja adecuadamente las vistas, que las transacciones guarden en la base de datos dentro del contenedor y que el visor cartográfico reciba los datos esperados.


### 8. Pruebas del Sistema (System Testing)
Verificación de la aplicación ejecutándose de forma integral en su entorno Docker. Evalúa flujos completos como inicio de sesión, navegación de rutas según el rol y respuesta del servidor en el puerto asignado.


### 9. Pruebas de Aceptación (User Acceptance Testing - UAT)
Validación final frente a los objetivos iniciales del proyecto. Corrobora que la plataforma oriente al usuario de forma clara sobre el transporte de Barinas y permita consultar información vial de forma intuitiva.


---


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
 http://localhost:8000`.

```


