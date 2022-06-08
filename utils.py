import marshmallow
from forecast import City
from schemas import RequestForecastSchema
from schemas import ResponseSchema

city=City()

def validate_fields(user_name,country):
    try:
        trim = lambda _value: None if _value=='' else _value
        info={'user_name':trim(user_name), 'country':trim(country)}
        info=RequestForecastSchema().load(info)
        return True,info
    except marshmallow.ValidationError as e:
        return False,e

def validate_get_city_information(**kwargs):
    valid,weather,temperature=city.get_city_information(kwargs['country'],kwargs['user_name'])
    if valid:
        return ResponseSchema(
            {'temperature':temperature,'weather':weather},
            'OK',
            False,
            201
        ).__dict__
    return ResponseSchema(
            {},
            f'{weather}'
    ).__dict__    
