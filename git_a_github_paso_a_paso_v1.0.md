### DE GIT A GITHUB: COMANDOS BASICOS

Esta guía práctica te llevará desde la configuración inicial de Git en tu computadora hasta la gestión de versiones de un proyecto de **Python** en **GitHub**. Git funciona capturando **instantáneas** (snapshots) de tu proyecto en momentos específicos, permitiéndote volver a ellas o colaborar con otros de forma eficiente.

### Fase 1: Configuración e Inicialización Local

Antes de empezar, debes preparar tu entorno y crear tu primer código fuente.

1.  **Establece tu identidad:** Configura tu nombre y correo para que Git sepa quién firma los cambios. Esto es inmutable en el historial.
    ```bash
    git config --global user.name "Tu Nombre"
    git config --global user.email "tu_email@ejemplo.com"
    ```
    1.1 **Visualizar la configuración global existente**
        ```bash
        git config --global --list
        ```
2.  **Crea el proyecto de Python:** Crea una carpeta y un archivo llamado `app.py`.
    *   **Código v1.0:**
        ```python
        print("Hola, Git y GitHub")
        ```
3.  **Inicializa el repositorio:** En la terminal, dentro de la carpeta del proyecto, ejecuta:
    ```bash
    git init
    ```
    Esto crea el subdirectorio `.git` que contiene el esqueleto del repositorio.

### Fase 2: El Ciclo de Confirmación (Versión 1.0)

El flujo de trabajo básico consiste en: modificar archivos, prepararlos y confirmarlos.

1.  **Revisa el estado:** Usa `git status` para ver que `app.py` está "sin rastrear" (untracked).
2.  **Prepara el archivo (Staging):** Mueve el archivo al área de preparación.
    ```bash
    git add app.py
    ```
3.  **Confirma los cambios:** Crea la primera instantánea permanente con un mensaje descriptivo.
    ```bash
    git commit -m "v1.0: Script inicial de Python"
    ```
4.  **Etiqueta la versión (Opcional):** Marca este punto como la versión 1.0.
    ```bash
    git tag -a v1.0 -m "Lanzamiento versión inicial"
    ```

### Fase 3: Carga del Proyecto a GitHub

Para compartir tu trabajo, necesitas un repositorio remoto.

1.  **Crea el repositorio en GitHub:** Ve a GitHub.com, pulsa el botón **"+"** y selecciona **"New repository"**. Ponle un nombre (ej. `mi-proyecto-python`) y pulsa **"Create repository"**.
2.  **Vincula el remoto:** Copia la URL de GitHub y asóciala al nombre corto "origin".
    ```bash
    git remote add origin https://github.com/tu-usuario/mi-proyecto-python.git
    ó
    git remote add origin git@github.com:tu-usuario/mi-proyecto-python.git  (Recomendación de github)
    ```
3.  **Sube el código:** Envía tu rama principal (usualmente `master` o `main`) al servidor.
    El parámetro -u (o --set-upstream) establece una relación de seguimiento entre tu rama local y la remota, facilitando futuros comandos de envío y 
    recepción. Este parametro solo se utiliza cuando se sube el código por primera vez.
    ```bash
    git push -u origin main
    ```

### Fase 4: Actualización a Nuevas Versiones (v1.1 y v1.2)

Ahora realizaremos cambios incrementales para simular el ciclo de vida del software.

#### Versión 1.1: Añadiendo una función
1.  **Modifica `app.py`:**
    ```python
    def saludar(nombre):
        return f"Hola, {nombre}"

    print(saludar("Usuario"))
    ```
2.  **Repite el ciclo:**
    ```bash
    git add app.py
    git commit -m "v1.1: Se añade función de saludo"
    git tag -a v1.1 -m "Funcion de saludo agg"
    git push origin main (o simplemente git push)
    ```

#### Versión 1.2: Mejora de la lógica
1.  **Modifica `app.py` de nuevo:**
    ```python
    def saludar(nombre):
        return f"¡Bienvenido, {nombre}! Estás usando Git."

    print(saludar("Programador"))
    ```
2.  **Confirma y sube:** Notese que en esta seccion en proceso de confirmacion y subida se realaiza en una sola instruccion con ayuda de la opcion '-am' 
    en   el comando commit.
    ```bash
    git commit -am "v1.2: Mensaje de saludo mejorado"
    git tag -a v1.2 -m "Mejora de la lògica"
    git push origin main
    ```
    *Nota: El comando `commit -am` permite preparar y confirmar archivos ya rastreados en un solo paso.*

3.  **Sincroniza etiquetas:** Si creaste etiquetas locales, envíalas al servidor.
    ```bash
    git push origin --tags
    ```

### Resumen de Comandos Útiles y de inspección técnica
*   **`git log --oneline`**: Visualiza tu historial de versiones de forma compacta.
*   **`git diff`**: Compara los cambios realizados en tu código antes de prepararlos.
*   **`git pull`**: Si trabajas con otros, usa esto para traer y combinar los cambios del servidor a tu equipo local.

*   **git log --oneline --decorate --graph`**: Visualiza de forma técnica y gráfica el historial de confirmaciones y dónde se encuentran los punteros 
     de las ramas y etiquetas
*   **git remote -v`**: Muestra las URLs asociadas a tus remotos para verificar la conexión con GitHub
