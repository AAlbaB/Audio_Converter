# Ejecución de la aplicación de forma local
En esta serie de instrucciones, se podrá ejecutar la aplicación de forma local en los sistemas operativos **Linux-Ubuntu** y **Windows**

## Contenedores de Docker
La aplicación requiere del servicio **Redis**, el cual puede ser usado mediante contenedores de Docker, estos serán validos para cualquier sistema operativo
1. Para crear el contenedor para Redis: `docker run --name redis-container -p 6379:6379 -d redis`

## Ejecutar aplicación en Ubuntu (Local)
Primero se debe realizar la instalación de algunos programas, para ello revisar el README de la raíz del proyecto.
Para el correcto funcionamiento del programa, se debe crear un ambiente virtual e instalar unos paquetes

### Preparar ambiente virtual (Estar en carpeta Backend)
1. Crear ambiente virtual en carpeta Backend: `python3 -m venv venv`
2. Activar ambiente virtual: `source venv/bin/activate`
3. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
4. Instalar requirements: `python3 -m pip install -r requirements.txt`
5. Verificar funcionalidad de redis: `redis-server`
6. Validar que redis este en ejecucion (salir con Q): `sudo systemctl status redis`

### Correr programa
**Importante:** Verificar que el entorno virtual este activado, verificar las conexiones a base de datos en el archivo *.env* y verificar que los contenedores (Si se utilizaron, estén funcionando adecuadamente)
1. Si se instaló redis adecuadamente pero no ejecuta, se debe abrir una consola y usar: `redis-server`
4. En una consola desde la carpeta Backend: `celery -A worker.tareas worker -l info`
5. En una consola desde la carpeta Backend: `flask run -p 3000` 

## Ejecutar aplicación en Windows (Local)
Primero se debe realizar la instalación de algunos programas, para ello revisar el README de la raíz del proyecto.
Para el correcto funcionamiento del programa, se debe crear un ambiente virtual e instalar unos paquetes

### Preparar ambiente virtual (Estar en carpeta Backend)
1. Crear ambiente virtual en carpeta Backend: `python -m venv venv`
2. Activar ambiente virtual: `venv/Scripts/activate`
3. En caso de tener problemas con activar el entorno virtual, se debe abrir el PowerShell como administrador y ejecutar el siguiente comando:  `Set-ExecutionPolicy RemoteSigned -Force`
4. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
5. Instalar requirements: `pip install -r requirements.txt`

### Correr programa
**Importante:** Verificar que el entorno virtual este activado, verificar las conexiones a base de datos en el archivo *.env* y verificar que los contenedores (Si se utilizaron, estén funcionando adecuadamente)
1. En una consola desde la carpeta Backend: `celery -A worker.tareas worker -l info --pool=solo`
2. En una consola desde la carpeta Backend: `flask run -p 3000` 
