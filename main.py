from api_calling.services.currency_services import get_currency_list
from api_calling.services.platform_token_services import get_platform_token_list, get_exchange_rate_token_realtime
from api_calling.reponse_json_format import CURRENCY, PLATFORM_TOKEN, EXCHANGE_RATE_REALTIME

# get_currency_list(CURRENCY)
# get_platform_token_list(PLATFORM_TOKEN)
print (get_exchange_rate_token_realtime("ethereum", "0xe41d2489571d322189246dafa5ebde1f4699f498", EXCHANGE_RATE_REALTIME))
