from Request_Get import Get_Request
import pprint
from prettytable import PrettyTable
import pandas as pd

#reading https://towardsdatascience.com/how-to-parse-json-data-with-python-pandas-f84fbd0b1025

LOCATIONS=["Bridgewatch","Lymhurst","Fort Sterling","Thetford","Martlock"]
FILE=".\Day25_Pandas\\Ores.txt"
EXCLUDED_QUALITY=["@4","@3","@2","@1"]
EXCLUDED_TIER=["T8","T7","T6"]


# import os #HINT: Clearing the Screen  os.system('cls')

# os.system('cls')

#--------------Function definitions--------------------
def best_trip(data,item):

    value_min=data[data.item_id==item].sell_price_min.min()
    city_min=data[data.sell_price_min==value_min].city
    value_max=data[data.item_id==item].sell_price_min.max()
    city_max=data[data.sell_price_min==value_max].city
    # date_min=data[data.sell_price_min==value_min].sell_price_min_date
    # date_max=data[data.sell_price_min==value_max].sell_price_min_date


    if value_min >0:

        # response= f"{item}  {city_min.values[0]}({value_min})-->{city_max.values[0]}({value_max}) {value_max-value_min}"
        response= [item, f"{city_min.values[0]}({value_min})-->{city_max.values[0]}({value_max})", value_max-value_min]
    else:
        response=[item, "Update Needed", 0]

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


# for exclusion in EXCLUDED:
#     for item in item_list:
#         if exclusion in item:
#             item_list.remove(item)
#             print(f"removed {item}")

for ex_quality in EXCLUDED_QUALITY:
    for ex_tier in EXCLUDED_TIER:
        for item in item_list:
            if (ex_quality in item and ex_tier in item)or "T5" in item and "@3" in item:
                item_list.remove(item)
                # print(f"removed {item}")

            
raw_response= make_request(item_list)
data= pd.json_normalize(raw_response)



table=PrettyTable()
table.field_names=["item_id","trip","profit"]

for item in item_list:
    if best_trip(data,item)[1]!="Update Needed":
            table.add_row(best_trip(data,item))
           

table.sortby="profit"
table.reversesort = True

print(data[data.item_id=="T2_ORE"])
print(table)


#--------------------Debug--------------------------
#pprint.pprint(response)
#/--------------------Debug--------------------------
 


