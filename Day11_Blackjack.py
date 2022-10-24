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
continue_playing=True
continue_playing_raw=""
cards=[11,2,3,4,5,6,7,8,9,10,10,10]

def refresh():
    os.system('cls')
    print(logo)

def betStart():
    total=bank_total
    bet_amount=0
    while bet_amount==0:
        bet_amount=int(input("How much do you want to bet?: $"))
        if bet_amount<=total:
            total-= bet_amount
        else:
            print("Try a smaller ammount")
    return total
    
def continue_playing_function():
    while continue_playing_raw!="y" and continue_playing_raw!="n":
        continue_playing_raw=input("Do you want to continue playing? (y/n): ").lower()
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

while continue_playing:
    refresh()
    print("Welcome to BlackJack!")
    print("Shuffling...")
    print("Bank: $"+str(bank_total))
    bank_total= betStart()

    # dealerHand=[]
    # playerHand=[]
    # gameRound=0

    #Computer and player first deal
    # for i in range(0,2):
    #     dealerHand=random_deal()
    #     playerHand=random_deal()
    # print(f"Dealer Hand: {dealerHand[0]},{dealerHand[1]}")
    # print(f"Dealer Hand: {playerHand[0]},{playerHand[1]}")

    continue_playing_function()
