import requests
import jsonschema
import ast
from api_calling.utils.response_parser import parse_response

def get_currency_list(currency_model):
    
    # declare currency list var so it will not die in scope
    currency_list = None    
    response_currency_api = requests.get('https://api.coingecko.com/api/v3/simple/supported_vs_currencies')

    # check if we can retrive the api successfully 
    try :
        currency_list = parse_response(response=response_currency_api)
    except Exception:
        raise Exception("Wrong URL or service down on api coigecko for currency API") 

    # check if json format is correctly
    try :
        jsonschema.validate(instance=currency_list, schema=currency_model)
    except jsonschema.ValidationError:
        raise jsonschema.ValidationError
        
    return currency_list

