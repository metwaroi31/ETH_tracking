import json
import requests
import jsonschema
from constant import MARKET_API
from api_calling.utils.response_parser import parse_response
from api_calling.utils.url_constructor import construct_url

def get_market_daily(parameters, model):
    market_daily = None
    request_url = construct_url(parameters=parameters, api=MARKET_API)
    market_daily_byte = requests.get(request_url)

    try :
        if market_daily_byte.status_code == 500:
            raise Exception("Wrong url or service down for api to get market value daily")
        market_daily = parse_response(response=market_daily_byte)
    except Exception:
        raise Exception("Wrong url or service down for api to get market value daily")

    try :
        jsonschema.validate(instance=market_daily, schema=model)
    except jsonschema.ValidationError:
        raise jsonschema.ValidationError

    return market_daily