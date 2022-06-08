from persistence import DB
from requests import request
import json
import os

db=DB()

class City:

    def _translate_errors(self,msg):
        msg=msg.strip().lower()
        if msg == 'api authorization failed': return 'Fallo autorizacion de API'
        if msg == 'you do not have permission to access this endpoint': return 'No tienes acceso a este endpoint'
        if msg == 'not found': return 'Recurso no encontrado'
        return msg

    def get_city_information(self,country,name):
        try:
            self._name=name
            self._country=country
            apikey=os.getenv("SECRET_KEY")
            params ={'apikey':apikey,'q':country,'language':'en-us'}
            payload=""
            method="GET"
            url = "http://dataservice.accuweather.com/locations/v1/cities/search"
            response = request(method, url, params=params, data=payload)
            if response.status_code == 200:
                data=response.json()
                return self.get_key_city(data)
            else:
                raise Exception(response.json()['Message'])
        except Exception as e:
            msg=self._translate_errors(str(e))
            return False,msg,None

    def get_key_city(self,data):
        data=(data[0]['Key'])
        return self.get_forecast_city(data)
        
    def get_forecast_city(self,data):
        apikey=os.getenv("SECRET_KEY")
        params={'apikey':apikey}
        payload=""
        method="GET"
        url = f"http://dataservice.accuweather.com/currentconditions/v1/{data}"
        response = request(method, url,params=params,data=payload)
        data=response.json()
        weather=data[0]["WeatherText"]
        temperature=f"{data[0]['Temperature']['Metric']['Value']}°{data[0]['Temperature']['Metric']['Unit']}"
        insert=self.insert_data_in_db(weather,temperature)
        if not insert:
            return False,"Error en la inserción de datos",None
        return True,weather,temperature

    def insert_data_in_db(self,weather,temperature):
        values=(self._name,self._country,weather,temperature)
        return db.insert_values_forecast(values)

