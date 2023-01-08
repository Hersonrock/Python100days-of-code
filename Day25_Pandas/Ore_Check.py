from Request_Get import Get_Request
import pprint
import pandas as pd

#reading https://towardsdatascience.com/how-to-parse-json-data-with-python-pandas-f84fbd0b1025

LOCATIONS=["Bridgewatch","Lymhurst","Fort Sterling","Thetford","Martlock"]
FILE=".\Day25_Pandas\\Ores.txt"


# import os #HINT: Clearing the Screen  os.system('cls')

# os.system('cls')

#--------------Function definitions--------------------
def best_trip(data,item):

    value_min=data[data.item_id==item].sell_price_min.min()
    city_min=data[data.sell_price_min==value_min].city
    value_max=data[data.item_id==item].sell_price_min.max()
    city_max=data[data.sell_price_min==value_max].city

    response= f"{item}\t {city_min.values[0]}({value_min})-->{city_max.values[0]}({value_max})\tprofit={value_max-value_min}"

    return response


def digest_txt():
    file = open(FILE)
    raw_file = file.read()
    file_list = raw_file.split()
    file.close()
    return file_list

def make_request(item_list):
    all_items=""
    location_constructor=f"locations={LOCATIONS[0]},{LOCATIONS[1]},{LOCATIONS[2]},{LOCATIONS[3]},{LOCATIONS[4]}"
    for item in item_list:
        all_items=all_items +"," +item
    item_constructor=f"{all_items}.json?"   
    endpoint = "stats/prices/"+item_constructor+location_constructor+"&qualities=1"
    response= Get_Request(endpoint)
    return response

item_list=digest_txt()

raw_response= make_request(item_list)
data= pd.json_normalize(raw_response)

for item in item_list:
    print(best_trip(data,item))

#--------------------Debug--------------------------
#pprint.pprint(response)
#/--------------------Debug--------------------------
 


