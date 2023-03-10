## Instalaciones
Se deben realizar las siguientes instalaciones para ejecutar el programa

**Nota:** Estas instrucciones e instalaciones son solo validas para instalacion en sistema operativo **Linux Ubuntu**

1. Actualizar paquetes: `sudo apt-get update`
2. Instalar Python 3.x: `sudo apt-get install python3`
3. Gestor de paquetes de python: `sudo apt-get install python3-pip`
4. Gestor de ambientes virtualesde python: `sudo apt-get install python3-venv`
5. Instalar paquete de flask: `sudo apt-get install python3-flask`
6. Servidor de redis: `sudo apt-get install redis-server` y `sudo systemctl enable redis-server.service`
7. Paquete de audios: `sudo apt-get install ffmpeg`

## Ejecutar aplicacion
Para el correcto funcionamiento del programa, se debe crear un ambiente virtual e instalar unos paquetes

### Preparar ambiente virutal (Estar en carpeta Backend)
1. Crear ambiente virtual en carpeta Backend:`python3 -m venv venv`
2. Activar ambiente virtual: `source venv/bin/activate`
3. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
4. Instalar requirements: `python3 -m pip install -r requirements.txt`
5. Verificar funcionalidad de redis: `redis-server`
6. Validar que redis este en ejecucion (salir con Q): `sudo systemctl status redis`

### Correr programa
**Importante:** Verificar que el entorno virtual este activado y verificar las conexiones a base de datos en el archivo .env
1. En una consola desde la carpeta Backend: `celery -A tareas worker -l info`
2. En caso de que no funcione celery, se debe tener otra consola corriendo redis: `redis-server`
2. En una consola desde la carpeta Backend: `flask run` 