# Ejecución de la aplicación de forma local
En esta serie de instrucciones, se podrá ejecutar la aplicación de forma local en los sistemas operativos **Linux-Ubuntu** y **Windows**

## Ejecutar aplicacion en Ubuntu (Local)
Primero se debe realizar la instalación de algunos programas, para ello revisar el README de la raiz del proyecto.
Para el correcto funcionamiento del programa, se debe crear un ambiente virtual e instalar unos paquetes

### Preparar ambiente virutal (Estar en carpeta Backend)
1. Crear ambiente virtual en carpeta Backend: `python3 -m venv venv`
2. Activar ambiente virtual: `source venv/bin/activate`
3. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
4. Instalar requirements: `python3 -m pip install -r requirements.txt`
5. Verificar funcionalidad de redis: `redis-server`
6. Validar que redis este en ejecucion (salir con Q): `sudo systemctl status redis`

### Correr programa
**Importante:** Verificar que el entorno virtual este activado y verificar las conexiones a base de datos en el archivo .env
1. En una consola desde la carpeta Backend: `celery -A tareas worker -l info`
2. En caso de que no funcione celery, se debe tener otra consola corriendo redis: `redis-server`
3. Si no hubo problemas con la instalación de redis, se puede usar un contenedor de docker con: `docker run --name redis-container -p 6379:6379 -d redis`
4. En una consola desde la carpeta Backend: `flask run` 

## Ejecutar aplicacion en Windows (Local)
Primero se debe realizar la instalación de algunos programas, para ello revisar el README de la raiz del proyecto.
Para la cuarta entrega entrega, se puede utilizar Windows, para esto seguir las siguientes instrucciones:

### Preparar ambiente virutal (Estar en carpeta Backend)
1. Crear ambiente virtual en carpeta Backend: `python -m venv venv`
2. Activar ambiente virtual: `venv/Scripts/activate`
3. En caso de tener problemas con activar el entorno virtual, se debe abrir el PowerShell como administrador y ejecutar el siguiente comando:  `Set-ExecutionPolicy RemoteSigned -Force`
4. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
5. Instalar requirements: `pip install -r requirements.txt`

### Correr programa
**Importante:** Verificar que el entorno virtual este activado y verificar las conexiones a base de datos en el archivo .env
1. Para Windows en necesario tener corriendo con Docker en el puerto 6379, debido a que Redis no esta soportado para Windows, se puede usar con el comando de Docker: `docker run --name redis-container -p 6379:6379 -d redis`
2. En una consola desde la carpeta Backend: `celery -A tareas worker -l info`
3. En una consola desde la carpeta Backend: `flask run` 
