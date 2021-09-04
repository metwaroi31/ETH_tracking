# from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import ValidationError
import requests
import jsonschema
from requests.models import requote_uri
from api_calling.utils.response_parser import parse_response
from api_calling.utils.url_constructor import construct_url 
from constant import DOMAIN, TOKEN_PLATFORM_API, TOKEN_ETHEREUM_PRICE_API

def get_platform_token_list(parameters, model):
    # initialize var so that it will live in scope
    platform_token_response_list = None
    requests_url = construct_url(parameters=parameters, api=TOKEN_PLATFORM_API)
    platform_token_response_byte = requests.get(requests_url)
    print (requests_url)
    # check if we can retrieve a list of platform token
    try :
        platform_token_response_list = parse_response(platform_token_response_byte)
    except Exception:
        raise Exception("Wrong url or service down on api coingecko to get list of platform token")

    # check if json format is correct
    try :
        jsonschema.validate(instance=platform_token_response_list, schema=model)
    except jsonschema.ValidationError:
        raise jsonschema.ValidationError
    
    return platform_token_response_list

def get_exchange_rate_token_realtime(parameters, model):
    # initialize var so that it will live in scope
    exchange_rate_real_time = None
    request_url = construct_url(parameters=parameters, api=TOKEN_ETHEREUM_PRICE_API)
    print(request_url)
    exchange_rate_byte = requests.get(request_url)
    
    try :
        exchange_rate_real_time = parse_response(exchange_rate_byte)
    except Exception:
        raise Exception("Wrong url or service down on api coingecko to get exchange rate real time")
    exchange_rate_real_time = parse_response(exchange_rate_byte)

    try :
        jsonschema.validate(instance=exchange_rate_real_time, schema=model)
    except jsonschema.ValidationError:
        raise jsonschema.ValidationError
    jsonschema.validate(instance=exchange_rate_real_time, schema=model)

    return exchange_rate_real_time
