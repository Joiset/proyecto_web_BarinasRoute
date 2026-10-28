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
Fase inicial donde se identificaron las necesidades del usuario. Se documentan los requerimientos funcionales, historias de usuario y la matriz de trazabilidad. Su fase de prueba asociada son las Pruebas de Aceptación, encargadas de confirmar que el sistema resuelva los problemas existentes.

### 2. Análisis del Sistema (System Analysis)

Traducción de los requisitos del usuario a especificaciones técnicas y operativas del software, definiendo límites del sistema, casos de uso y diagramas de flujo. Se vincula con las Pruebas del Sistema, las cuales validan el comportamiento global de la aplicación de extremo a extremo.

### 3. Diseño de Software / Arquitectura (Software Design)

Definición de la arquitectura tecnológica general: estructura modular desacoplada en Django, persistencia en base de datos relacional y contenedorización de servicios con Docker. Se asocia con las Pruebas de Integración, destinadas a comprobar la comunicación correcta entre los módulos del sistema y servicios externos.

### 4. Diseño de Módulos (Module Design)

Especificación de bajo nivel de cada componente individual: definición de tablas y esquemas relacionales (models.py), lógica de control (views.py), validación de entradas (forms.py) y mapeo de endpoints (urls.py). Su fase de prueba correspondiente son las Pruebas Unitarias, verificando que las funciones y métodos operen correctamente de forma aislada.

### Punto de Inflexión: Codificación (Coding)

Etapa de implementación técnica donde se construyen los módulos en código Python/Django sobre Docker, aplicando estándares limpios de desarrollo y control de versiones con Git. 


### Despliegue Local con Docker

#### 1. Clonar el repositorio:
```bash
git clone https://github.com/Joiset/proyecto_web_JOI.git
cd proyecto_web_JOI
```

#### 2. Instalar dependencias del frontend (Vite.js):
```bash
cd frontend
npm install
cd ..
```

#### 3. Construir la imagen del proyecto:
```bash
docker compose build
```

#### 4. Ejecutar migraciones de la base de datos:
```bash
docker compose run --rm web python manage.py migrate
```

#### 5. Crear usuario administrador:
```bash
docker compose run --rm web python manage.py createsuperuser
```

#### 6. Iniciar el servidor:
```bash
docker compose up
```

Una vez iniciado el contenedor, la aplicación estará disponible en tu navegador en:  
**http://localhost:8000**


