### PERSONAL ACCESS TOKENS: GENERACIÓN Y FORMA DE USO

Desde hace un par de años, **GitHub** dejó de aceptar tu contraseña normal para operaciones desde la terminal por razones de seguridad.
Ahora, en lugar de tu clave de siempre, debes usar un **Personal Access Token (PAT)**. Aquí te explico cómo aplicarlo paso a paso:

***1. Generar tu Token en GitHub***
Entra a tu cuenta de GitHub desde el navegador.

    1. Ve a Settings (Configuración) > Developer Settings (abajo del todo a la izquierda).
    2. Selecciona Personal access tokens > Tokens (classic).
    3. Haz clic en Generate new token (puedes elegir "classic").
    4. Ponle un nombre (ej. "Mi PC Linux") y selecciona los permisos. Para lo que estás haciendo, marca la casilla repo (esto da control total sobre tus 
        repositorios privados y públicos).
    5. Haz clic en Generate token.

IMPORTANTE: Copia el token que aparece (es una serie de letras y números). Solo se muestra una vez; si lo pierdes, tendrás que crear otro.

***2. Usar el Token en la Terminal***
    Ingresa el comando:
    ```bash
    git push -u origin main
    ```
    Username: usuario
    Password: Pega aquí el Token que acabas de copiar (no verás que se escriban caracteres, es normal).

***3. Cómo evitar escribir el Token cada vez***
En Linux, lo ideal es que Git "recuerde" las credenciales para no tener que pegar ese código largo en cada operación. Puedes activar el asistente de credenciales con este comando:
    ```bash
    git config --global credential.helper store
    ```
    La próxima vez que hagas un push y metas el token, Git lo guardará de forma permanente en tu sistema
    El mensaje Password authentication is not supported es la forma que tiene GitHub de decirte que la "puerta" de las contraseñas está cerrada y ahora solo se entra con "llaves digitales" (tokens).

    Si tienes pensado trabajar mucho con Git en este entorno, otra opción excelente a futuro es configurar una Llave SSH, que es incluso más segura y cómoda que los tokens, pero por ahora, con el PAT podrás subir tu script sin problemas.
