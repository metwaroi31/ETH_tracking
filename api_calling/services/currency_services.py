import requests
import jsonschema
from constant import CURRENCY_API
from api_calling.utils.response_parser import parse_response
from api_calling.utils.url_constructor import construct_url

def get_currency_list(model):
    # declare currency list var so it will not die in scope
    currency_list = None    
    request_url = construct_url(api=CURRENCY_API)
    response_currency_api = requests.get(request_url)

    # check if we can retrive the api successfully 
    try :
        if response_currency_api.status_code == 500:
            raise Exception("Wrong URL or service down on api coigecko for currency API") 
        currency_list = parse_response(response=response_currency_api)
    except Exception:
        raise Exception("Wrong URL or service down on api coigecko for currency API") 

    # check if json format is correctly
    try :
        jsonschema.validate(instance=currency_list, schema=model)
    except jsonschema.ValidationError:
        raise jsonschema.ValidationError
        
    return currency_list

