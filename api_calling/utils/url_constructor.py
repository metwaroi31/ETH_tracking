from constant import DOMAIN

def construct_query_params(param_dict):
    return_query_string = ""
    for key in param_dict.keys():
        return_query_string += key
        return_query_string += "="
        return_query_string += param_dict.get(key)
        return_query_string += "&"
    return return_query_string

def construct_url(parameters=None, api=None):
    return_url = None
    if parameters:
        return_url = DOMAIN + api + "?"
        query_params = construct_query_params(parameters)
        return_url += query_params
    else :
        return_url = DOMAIN + api
    return return_url