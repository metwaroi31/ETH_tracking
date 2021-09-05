from constant import DOMAIN

def construct_query_params(param_dict):
    return_query_string = ""
    for key in param_dict.keys():
        if key != "id":
            return_query_string += key
            return_query_string += "="
            return_query_string += str(param_dict.get(key))
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

    if "id" in parameters.keys():
        return_url = return_url.replace("replacing_id", parameters.get("id"))
        
    return return_url