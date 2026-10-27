### BarinasRoute - Plataforma de Gestión de Movilidad Urbana

**Asignatura:** Desarrollo de Aplicaciones Web I  
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

Esta fase inicial se centra en recopilar, examinar y documentar detalladamente las necesidades del usuario final y las reglas de negocio de la aplicación. Genera como entregables principales el Documento de Especificación de Requisitos de Software (SRS), las historias de usuario y la matriz de trazabilidad. Su fase de prueba asociada son las Pruebas de Aceptación, las cuales validan formalmente que la solución desarrollada resuelva los problemas reales planteados por los usuarios.

### 2. Análisis del Sistema (System Analysis)

En esta etapa se traducen las necesidades recabadas del usuario a especificaciones técnicas y funcionales estructuradas, delimitando los alcances y las interfaces de entrada y salida del software. Entrega casos de uso, diagramas de flujo de datos y descripciones del comportamiento global del sistema. Se vincula de forma directa con las Pruebas del Sistema, encargadas de comprobar el funcionamiento integral de la aplicación de extremo a extremo.

### 3. Diseño de Software / Arquitectura (Software Design)

Aquí se establece la estructura tecnológica general del proyecto, definiendo la interacción entre las distintas capas (frontend, backend y base de datos) y la infraestructura requerida para su despliegue. Sus entregables abarcan diagramas de componentes, la selección y justificación del stack tecnológico (Python, Django, Bootstrap 5, Docker y base de datos relacional) y la definición de protocolos de comunicación. Se asocia con las Pruebas de Integración, cuyo objetivo es verificar la comunicación fluida entre módulos internos y servicios externos.

### 4. Diseño de Módulos (Module Design)

Consiste en la especificación técnica de bajo nivel para cada componente individual, abordando su lógica interna, algoritmos y estructuras de almacenamiento de datos. Como entregables produce los esquemas de base de datos (`models.py`), la lógica de control (`views.py`), los formularios de validación (`forms.py`) y el direccionamiento de rutas (`urls.py`). Su fase de prueba correspondiente son las Pruebas Unitarias, destinadas a corroborar que cada función, clase y método opere correctamente de manera aislada.

### Punto de Inflexión: Codificación (Coding)

Representa el momento donde se materializan todas las especificaciones y diseños previos en código fuente ejecutable, implementando buenas prácticas de desarrollo, gestión de control de versiones y entornos de ejecución aislados mediante contenedores Docker.

---

### 5. Pruebas Unitarias (Unit Testing)

Corresponde a la primera etapa de validación tras la codificación, enfocada en examinar bloques de código aislados e independientes. Valida la lógica interna de métodos en modelos, señales automáticas de usuario, funciones de cálculo geoespacial y validaciones de formularios antes de que interactúen con el resto del sistema.

### 6. Pruebas de Integración (Integration Testing)

Verifica que los módulos individuales interactúen de forma correcta y armónica entre sí al combinarse. Asegura que la capa de autenticación transmita los roles adecuadamente hacia las vistas, que las consultas al ORM sincronicen con el motor de base de datos dentro del contenedor y que los endpoints suministren las estructuras de datos esperadas por el visor cartográfico.

### 7. Pruebas del Sistema (System Testing)

Evalúa el comportamiento global de la plataforma ejecutándose de manera integral en su entorno contenerizado. Comprueba flujos completos de inicio a fin, tales como el registro de ciudadanos, la asignación de permisos según el perfil, la emisión de alertas de contingencia vial y las respuestas del servidor ante peticiones concurrentes en el puerto expuesto.

### 8. Pruebas de Aceptación (User Acceptance Testing - UAT)

Constituye la fase final de verificación donde se evalúa el software frente a los objetivos y requerimientos planteados originalmente por los usuarios y la comunidad. Valida que BarinasRoute cumpla con orientar efectivamente sobre las rutas urbanas, advertir con precisión las bifurcaciones y permitir una interacción fluida y accesible desde cualquier navegador.

---

## Instrucciones de Instalación y Despliegue Local

1. **Clonar el repositorio:**


```bash
git clone [https://github.com/Joiset/proyecto_web_JOI.git](https://github.com/Joiset/proyecto_web_JOI.git)
cd proyecto_web_JOI

```


2. **Construir la imagen de Docker:**
```bash
docker compose build

```


3. **Ejecutar migraciones de la base de datos:**
```bash
docker compose run --rm web python manage.py migrate

```


4. **Crear usuario administrador:**
```bash
docker compose run --rm web python manage.py createsuperuser

```


5. **Iniciar el servidor:**
```bash
docker compose up

```


*Acceder a la aplicación desde el navegador en `http://localhost:8000`.*



```

```