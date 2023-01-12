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
1. Si hubo problemas con la instalación de redis, se puede usar un contenedor de docker con: `docker run --name redis-container -p 6379:6379 -d redis`
2. El proyecto usa a una base de datos Posgres, en caso de no tenerlo configurado en el equipo, se puede usar Docker Compose en la ruta: `Audio_Converter/Backend/database`  y usar el comando: `docker compose up -d`, para asi levantar un contenedor de Postgres
3. Si se instaló redis adecuadamente pero no ejecuta, se debe abrir una consola y usar: `redis-server`
4. En una consola desde la carpeta Backend: `celery -A worker.tareas worker -l info`
5. En una consola desde la carpeta Backend: `flask run` 

## Ejecutar aplicacion en Windows (Local)
Primero se debe realizar la instalación de algunos programas, para ello revisar el README de la raiz del proyecto.
Para el correcto funcionamiento del programa, se debe crear un ambiente virtual e instalar unos paquetes

### Preparar ambiente virutal (Estar en carpeta Backend)
1. Crear ambiente virtual en carpeta Backend: `python -m venv venv`
2. Activar ambiente virtual: `venv/Scripts/activate`
3. En caso de tener problemas con activar el entorno virtual, se debe abrir el PowerShell como administrador y ejecutar el siguiente comando:  `Set-ExecutionPolicy RemoteSigned -Force`
4. Validar en la consola que se tiene activo el ambiente virtual, para desactivar env: `deactivate`
5. Instalar requirements: `pip install -r requirements.txt`

### Correr programa
**Importante:** Verificar que el entorno virtual este activado y verificar las conexiones a base de datos en el archivo .env
1. Para Windows en necesario tener corriendo en el puerto **6379** Redis, se puede usar con el comando de Docker: `docker run --name redis-container -p 6379:6379 -d redis`
2. El proyecto usa a una base de datos Posgres, en caso de no tenerlo configurado en el equipo, se puede usar Docker Compose en la ruta: `Audio_Converter/Backend/database`  y usar el comando: `docker compose up -d`, para asi levantar un contenedor de Postgres
3. En una consola desde la carpeta Backend: `celery -A worker.tareas worker -l info --pool=solo`
4. En una consola desde la carpeta Backend: `flask run` 
