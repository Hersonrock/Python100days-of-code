logo = """           _ _     _               _    _ _       _                 _                               _____                      
     /\   | | |   (_)             | |  | (_)     | |               | |                             / ____|                     
    /  \  | | |__  _  ___  _ __   | |__| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __  | |  __  __ _ _ __ ___   ___ 
   / /\ \ | | '_ \| |/ _ \| '_ \  |  __  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__| | | |_ |/ _` | '_ ` _ \ / _ \
  / ____ \| | |_) | | (_) | | | | | |  | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |    | |__| | (_| | | | | | |  __/
 /_/    \_\_|_.__/|_|\___/|_| |_| |_|  |_|_|\__, |_| |_|\___|_|    |______\___/ \_/\_/ \___|_|     \_____|\__,_|_| |_| |_|\___|
                                             __/ |                                                                             
                                            |___/                                                                              """

#Based of MMORPG https://albiononline.com/en/home , Api https://www.albion-online-data.com/api/swagger/index.html

#Using "requests" , installed with command "pip install requests"
#   see: https://www.geeksforgeeks.org/get-post-requests-using-python/
#Using Item List
#   https://github.com/broderickhyman/ao-bin-dumps/blob/master/formatted/items.txt

import requests  # used for sending requests to the API
import json # used for manipulating JSON data
import pprint    # used for formatting the output of JSON objects received in API responses
import random


DATA_URL = 'https://www.albion-online-data.com/api/v2/stats/Prices/'
LOCATION_RAW = '?locations=Fort+Sterling'
LOCATION='Fort Sterling'
QUALITY = '&qualities=1'
MAX_TIER=8

lose=False

#Test request https://albion-online-data.com/api/v2/stats/Prices/T4_CAPE?locations=Fort%20Sterling&qualities=1

item_list= ["ORE","HIDE","FIBER","WOOD","ROCK"]

def item_get(tier,item):
     
     item= (f"T{tier}_"+item)

     return item

def item_cost(tier,item):
     response = requests.get(DATA_URL+item_get(tier,item_list[item])+LOCATION_RAW+QUALITY)
     data=response.json()
     return data[0]["sell_price_min"]

while not lose:
     item1=0
     item2=0
     random_tier=random.randint(1,MAX_TIER)
     while item1==item2:
          item1=random.randint(0,4)
          item2=random.randint(0,4)

     item1_cost= item_cost(random_tier,item1)
     item2_cost= item_cost(random_tier,item2)


     print("In " + LOCATION + ", which one costs the most?")

     choice=int(input(f"T{random_tier}_{item_list[item1]} or T{random_tier}_{item_list[item2]} 1 Or 2?: "))
     print(f"T{random_tier}_{item_list[item1]} costs: {item1_cost}")
     print(f"T{random_tier}_{item_list[item2]} costs: {item2_cost}")

     if(item1_cost>item2_cost):
          more_expensive=1
     elif(item1_cost<item2_cost):
          more_expensive=2
     else:
          more_expensive=0

     if more_expensive!=0:
          if more_expensive!=choice:
               print("Wrong, you lose")
               lose=True
          else:
               print("Nice,you know the market")
     else:
          print("They actually cost the same today")

     


print("Thanks for playing")
