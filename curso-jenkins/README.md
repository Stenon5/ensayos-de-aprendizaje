# Curso de Jenkins

Trabajos olvidados del curso de Jenkins de Platzi. Instalé Jenkins de dos formas y armé los ejercicios del curso. Aquí está solo la configuración de cada trabajo, el `config.xml` que guarda Jenkins. No hay credenciales.

## Qué hice

`como-servicio/`, con Jenkins instalado como servicio del sistema:

- `hello-platzi`: un trabajo con un parámetro de nombre que saluda y luego dispara otro trabajo.
- `Parametrized`: recibe un parámetro desde otro trabajo.
- `watchers`: corre cuando `hello-platzi` termina bien.

`desde-war/`, con Jenkins ejecutado desde el archivo `jenkins.war`:

- `parametrized`: el mismo ejercicio de parámetros.
- `test-sum-nodejs`: descarga el repo de ejemplo del profesor, instala con npm y corre las pruebas cuando hay cambios en GitHub.
- `test-pipeline-sum-node`: lo mismo como pipeline.

## Cómo usarlo

En un Jenkins con los plugins de Git, GitHub, Pipeline y Parameterized Trigger, crea un trabajo con el mismo nombre y reemplaza su `config.xml` con el de aquí, en `$JENKINS_HOME/jobs/<nombre>/`. Después recarga la configuración desde "Administrar Jenkins".
