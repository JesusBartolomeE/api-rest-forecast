# API REST para consultar el clima

* API REST para consultar el clima de un país.
* Se consume el servicio del clima de la API de AccueWeather.
* Revise la sección de consideraciones de este documento.

# Stack

* Pytohn
* Flask
* SQLite

## Comenzando

* Clone el repositorio

        git clone https://github.com/JesusBartolomeE/api-rest-forecast.git 

## Instalación

* Ubique la carpeta donde clono el repositorio.

        cd api-rest-forecast/

* Cree su entorno virtual.

        virtualenv venv -p python3

* Active el entorno virtual creado.

        source venv/bin/activate 

* Ejecute Requirements.txt

        pip install -r requirements.txt

* Antes de iniciar el servidor revise la sección de consideraciones.

* Inicie el servidor.

        python3 app.py

## Consideraciones

* Se debe tener una cuenta en [AccueWeather](https://developer.accuweather.com/), para obtener una API Key valida.
* Después de clonar el repositorio y antes de que inicie el servidor, debe de realizar los siguientes pasos.

* Se debe crear el archivo .env y colocar la API Key en la variable SECRET_KEY.

              export SECRET_KEY='XXXXXXXXXXXXXXX'

* Ejecute el comando.

                source .env

* Listo, puede inicar el servidor.

## Pruebas
* Para iniciar tests de funcionalidad es necesario contar con [Postman](https://www.postman.com/) instalado

* Ejecute en Postman el archivo TEST_API_FORECAST.json

* Inicie el set de pruebas.