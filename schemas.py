from dataclasses import dataclass
from dataclasses import field
from typing import Optional
from marshmallow import Schema
from marshmallow import fields
from typing import List


class RequestForecastSchema(Schema):
    user_name=fields.Str(required=True, allow_none=False)
    country=fields.Str(required=True,allow_none=False)

@dataclass
class ResponseSchema:
    result:dict  
    message:str
    error:bool =field(default=True)
    statusCode:int = field(default=500)
