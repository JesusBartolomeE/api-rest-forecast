from flask import Flask
from flask import request
from forecast import City
from search import Search
from utils import validate_fields
from flask import jsonify
from schemas import ResponseSchema
from utils import validate_get_city_information

app = Flask(__name__)
app.secret_key = 'mysecretkey'

city=City()
search=Search()

@app.route('/')
def main():

    return "Server conecction"

@app.route('/get-forecast', methods=['POST'])
def get_forecast():
    try:
        if request.method=='POST':
            user_name=request.json['name']
            country=request.json['country']
            valid,fields=validate_fields(user_name,country)
            if valid:
                response=validate_get_city_information(**fields)
                return response
            else:
                return ResponseSchema({}, f'{fields}').__dict__
    except Exception as e:
        return ResponseSchema({},f'{e}').__dict__    

@app.route('/check-history', methods=['GET'])    
def check_history():
    if request.method=='GET':
        kwargs = request.args
        try:
            data,query=search.search_in_db(**kwargs)
            return ResponseSchema(
                {'data':data,'count':len(data),'query':query,},
                'OK',
                False,
                200
            ).__dict__    
        except Exception as e:
            return ResponseSchema({},f'{e}').__dict__

if __name__=='__main__':

    app.run(debug = True, port = 8000)     

