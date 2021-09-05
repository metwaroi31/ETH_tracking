from api_calling.services.currency_services import get_currency_list
from api_calling.services.platform_token_services import get_exchange_rate_token_daily, get_platform_token_list, get_exchange_rate_token_realtime
from api_calling.reponse_json_format import CURRENCY, PLATFORM_TOKEN, EXCHANGE_RATE_REALTIME, EXCHANGE_RATE_DAILY

# TO DO : tranform into excel files based on DDL

parameters_price_api = {
    "contract_addresses" : "0xe41d2489571d322189246dafa5ebde1f4699f498",
    "vs_currencies" : "usd",
    "include_market_cap" : "true",
    "include_24hr_vol" : "true",
    "include_24hr_change" : "true",
    "include_last_updated_at" : "true",
}

parameters_platform_token_list = {
    "include_platform" : "true"
}

parameters_price_daily_api = {
    "id" : "",
    "vs_currencies" : "usd",
    "days" : 7
}

# print (get_currency_list(model=CURRENCY))
# print (get_platform_token_list(parameters=parameters_platform_token_list,model=PLATFORM_TOKEN))
# print (get_exchange_rate_token_realtime(parameters=parameters_price_api, model=EXCHANGE_RATE_REALTIME))
print (get_exchange_rate_token_daily(parameters=parameters_price_daily_api, model=EXCHANGE_RATE_DAILY))
