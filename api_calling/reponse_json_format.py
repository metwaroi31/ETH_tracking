# used to validate data from API 

CURRENCY = {
    "type" : "array",
    "items" : {
        "type" : "string"
    }
}

PLATFORM_TOKEN = {
    "type" : "array",
    "items" : {
        "type" : "object",
        "properties" : {
            "id" : {"type" : "string"},
            "symbol" : {"type" : "string"},
            "name" : {"type" : "string"},
            "platforms" : {
                "type" : "object"
            },
        "additionalProperties" : True
        }
    }
}

# This model has bug please work on this
EXCHANGE_RATE_REALTIME = {
    "type" : "object", 
    "properties" : {
        "^" : {"type" : "string"},
        ".*\market_cap$" : {"type" : "string"},
        ".*\\24h_volume$" : {"type" : "string"},
        ".*\\24h_change$" : {"type" : "string"},
        "last_updated_at" : {"type" : "integer"}
    },
}

