# from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import ValidationError
import requests
import jsonschema
from api_calling.utils.response_parser import parse_response

def get_platform_token_list(token_platform_model):
    # initialize var so that it will live in scope
    platform_token_response_list = None
    platform_token_response_byte = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    
    # check if we can retrieve a list of platform token
    try :
        platform_token_response_list = parse_response(platform_token_response_byte)
    except Exception:
        raise Exception("Wrong url or service down on api coingecko to get list of platform token")

    # check if json format is correct
    try :
        jsonschema.validate(instance=platform_token_response_list, schema=token_platform_model)
    except jsonschema.ValidationError:
        raise jsonschema.ValidationError
    
    return platform_token_response_list

def get_exchange_rate_token_realtime(platform, platform_address, exchange_rate_real_time_model):
    exchange_rate_real_time = None
    exchange_rate_byte = requests.get("https://api.coingecko.com/api/v3/simple/token_price/" + platform + "?contract_address=" + platform_address)

    try :
        exchange_rate_real_time = parse_response(exchange_rate_byte)
    except Exception:
        raise Exception("Wrong url or service down on api coingecko to get exchange rate real time")

    try :
        jsonschema.validate(instance=exchange_rate_real_time, schema=exchange_rate_real_time_model)
    except jsonschema.ValidationError:
        raise jsonschema.ValidationError

    return exchange_rate_real_time

# def get_exchange_rate_token_history(token, number_of_days, exchange_rate_daily_model):
#     exchange_rate_daily = None
#     exchange_rate_daily_byte = requests.get("https://api.coingecko.com/api/v3/coins/" + token + "/ohlc" + )
#     return