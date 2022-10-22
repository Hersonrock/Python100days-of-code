logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import os
import random

#HINT: Clearing the Screen
#   os.system('cls')

bank_total=1000
bet_ammount=0
continue_playing=True
continue_playing_raw=""

cards=[11,2,3,4,5,6,7,8,9,10,10,10]

def refresh():
    os.system('cls')
    print(logo)

def betStart():
    while bet_ammount==0:
        bet_ammount=int(input("How much do you want to bet?: "))
        if bet_ammount<=bank_total:
            bank_total -=bet_ammount
        else:
            print("Try a smaller ammount")
    
def continue_playing_function():
    while continue_playing_raw!="y" and continue_playing_raw!="n":
        continue_playing_raw=input("Do you want to continue playing? (y/n): ").lower
        if continue_playing_raw=="y":
            continue_playing=True
        elif continue_playing_raw=="n":
            continue_playing=False
        else:    
            print("Invalid Option")
    continue_playing_raw=""

def random_deal():
    first_deal= random.randint(0,11)
    return cards[first_deal]

def computer_deal():
    card1=random_deal()
    card2=random_deal()
    return [card1,card2]   
    ##Working here.....

while continue_playing:
    refresh()
    print("Welcome to BlackJack!")
    print("Shuffling...")
    print("Bank: $"+str(bank_total))
    betStart()

    continue_playing_function()
