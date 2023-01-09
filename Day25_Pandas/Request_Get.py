import requests # used for sending requests to the API
import json # used for manipulating JSON data

def Get_Request(endpoint):
    uri= f"https://www.albion-online-data.com/api/v2/{endpoint}"
    #--------Debug-------
    #print(uri)
    #--------------------
    return requests.get(uri).json()

