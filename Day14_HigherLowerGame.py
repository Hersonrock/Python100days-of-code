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

DATA_URL = 'https://www.albion-online-data.com/api/v2/stats/Prices/'
LOCATION = '?locations=Fort%20Sterling'
QUALITY = '&qualities=1'

response = requests.get(DATA_URL+'T4_CAPE'+LOCATION+QUALITY).json()
print (response)
