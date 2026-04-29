Laboratorio práctico para la ejercitación de los comandos Git y la carga de el proyecto Github.

Basado en el desarrollo de este laboratorio y el material de las fuentes, a continuación se presenta un resumen técnico de los comandos utilizados para gestionar el ciclo de vida de un proyecto en Git y GitHub:

1. Configuración de Identidad
Antes de iniciar, se establece la identidad del usuario, la cual se vincula de forma inmutable a cada confirmación de cambios
.
git config --global user.name "Nombre": Configura el nombre del autor
.
git config --global user.email "correo@ejemplo.com": Configura el correo electrónico del autor
.
2. Inicialización y Preparación Local
Este grupo de comandos permite convertir una carpeta en un repositorio y gestionar el área de preparación (staging area)
.
git init: Crea un nuevo repositorio de Git en el directorio actual, generando la carpeta oculta .git
.
git status: Muestra el estado de los archivos: si están modificados, preparados (staged) o sin rastrear (untracked)
.
git add <archivo>: Añade el contenido de un archivo al área de preparación para la próxima confirmación
.
git add .: Añade todos los cambios y archivos nuevos del directorio actual al área de preparación
.
3. Confirmación de Cambios (Commit) y Versiones
Estos comandos registran instantáneas permanentes del proyecto en la base de datos local
.
git commit -m "mensaje": Crea una nueva confirmación con los cambios que están en el área de preparación
.
git commit -am "mensaje": Atajo que prepara automáticamente todos los archivos rastreados y los confirma en un solo paso
.
git tag -a v1.0 -m "mensaje": Crea una etiqueta anotada, que funciona como un marcador permanente para hitos importantes como lanzamientos de versión
.
4. Conexión con GitHub y Sincronización Remota
Permiten compartir el trabajo local con un servidor remoto en GitHub
.
git remote add origin <URL>: Asocia el repositorio local con un repositorio remoto bajo el alias "origin"
.
git push -u origin master: Sube los cambios por primera vez y establece una relación de seguimiento (upstream) entre la rama local y la remota
.
git push origin master: Envía las confirmaciones locales a la rama principal del servidor una vez establecida la vinculación
.
git push origin --tags: Transfiere al servidor remoto todas las etiquetas de versión creadas localmente
.
5. Inspección y Seguimiento
Comandos esenciales para revisar el historial y las diferencias en el código
.
git log --oneline: Visualiza el historial de confirmaciones de forma compacta en una sola línea
.
git diff: Muestra las líneas exactas que han sido añadidas o eliminadas en los archivos modificados pero aún no preparados
.
git remote -v: Muestra las direcciones URL que Git tiene almacenadas para los nombres de los remotos
.
