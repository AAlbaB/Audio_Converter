# Convertidor de audio
Este proyecto es la modificación a las entregas realizadas para la asignatura 'Desarrollo de software en la nube'. El objetivo de este proyecto es reforzar lo aprendido.
El objetivo de esta aplicación es convertir audios mp3, wav y ogg, mediante el uso de colas de tareas usando Redis.

## Instalaciones Linux (Ubuntu)
Se deben realizar las siguientes instalaciones para ejecutar el programa

1. Actualizar paquetes: `sudo apt update`
2. Instalar Python 3.x: `sudo apt install python3`
3. Instalar gestor de paquetes de python: `sudo apt install python3-pip`
4. Instalar gestor de ambientes virtualesde python: `sudo apt install python3-venv`
5. Instalar paquete de flask: `sudo apt install python3-flask`
6. Instalar servidor de redis: `sudo apt install redis-server` y `sudo systemctl enable redis-server.service`
7. Instalar paquete de audios: `sudo apt install ffmpeg`
8. Instalar Git: `sudo apt install git`

## Instalaciones Windows
Para esta entrega se puede utilizar de forma local en sistema operativo windows, para ello se debe realizar las siguientes instalaciones

1. Descargar e instalar python 3.9.8: [AQUI](https://www.python.org/downloads/release/python-398/)
2. Descargar e instalar Git: [AQUI](https://git-scm.com/download/win)
3. Descargar e instalar ffmpeg: [AQUI](https://www.wikihow.com/Install-FFmpeg-on-Windows), verificar instalación con: `ffmpeg -version`

**Nota:** Para continuar con la ejecución del programa, se debe ingresar a la carpeta **Backend** y leer el archivo *README* que allí se encuentra.

## Peticiones a la API
1. Creación de un usuario: POST ```/api/auth/signup```
2. Ingreso de usuario: POST ```/api/auth/login```
3. Ver todas las tareas de un usuario: GET ```/api/tasks```
4. Crear una tarea de un usuario: POST ```/api/tasks```
5. Ver una tarea específica: GET ```/api/tasks/<int:id_task>```
6. Actualizar una tarea específica: PUT ```/api/tasks/<int:id_task>```
7. Eliminar una tarea específica: DELETE ```/api/tasks/<int:id_task>```
8. Descargar un archivo GET ```/api/files/<string:fileName>```
9. Para obtener la colección de los servicios ir a la carpeta **Collections** del proyecto y descargar los dos archivos en formato *JSON*
10. Una vez descargados, ir a la aplicación `Postman > File > Import > Cargar archivo JSON`