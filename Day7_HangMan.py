#Using random word API from
#   http://random-word-api.herokuapp.com/home
#    https://random-word-api.herokuapp.com/word
#Using "requests" , installed with command "pip install requests"
#   see: https://www.geeksforgeeks.org/get-post-requests-using-python/

import requests
randomWordURL = "https://random-word-api.herokuapp.com/word"
randomWordRAW = requests.get(url=randomWordURL)
randomWordStringRaw= randomWordRAW.text
randomWordString=randomWordStringRaw[2:-2]
print (randomWordString)


