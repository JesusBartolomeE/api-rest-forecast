# API REST para consultar el clima

* API REST para consultar el clima de un país.
* Se consume el servicio del clima de la API de AccueWeather.
* Revise la sección de consideraciones.

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

* Inicie el servidor.

        python3 app.py

## Pruebas

## Consideraciones

* Se debe tener una cuenta en [AccueWeather](https://developer.accuweather.com/), para que se pueda obtener una llave de acceso valida.
* Si ya cuenta con una llave de acceso, guardela en una variable de entorno y indiquela en:

                forecast.py/apikey=os.getenv("SECRET_KEY")

