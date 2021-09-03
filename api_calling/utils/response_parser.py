import json
# import 

def parse_response(response):
    # convert byte to json or list
    content_of_response = response.content
    # print (content_of_response)
    content_of_response = content_of_response.decode('utf-8')
    response_json = json.loads(content_of_response)
    # print (response_json)
    return response_json
