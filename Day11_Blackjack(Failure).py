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
continue_hand=True
cards=[11,2,3,4,5,6,7,8,9,10,10,10]

def refresh():
    os.system('cls')
    print(logo)

def betStart():
    global bet_ammount
    global bank_total
    while bet_ammount==0:
        bet_ammount=int(input("How much do you want to bet?: $"))
        if bet_ammount<=bank_total:
            bank_total -=bet_ammount
        else:
            print("Try a smaller ammount")
            bet_ammount=0
    
def continue_playing_function():
    global continue_playing
    global continue_playing_raw
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

def win_check(total):
    if total==21:
        return True
    else:
        return False
def ace_check_when_losing(hand):
    total_score=0
    check=0
    for card in hand:
        total_score +=card
        if card==11:
            check+=1
    if total_score>21 and check!=-1:
        return True

def  computer_auto():
    while dealer_hand_total<21:
        dealer_hand.append(random_deal())
        dealer_hand_total += dealer_hand[round-1]
        round+= 1 
        if ace_check_when_losing(dealer_hand):
            dealer_hand_total-=10
            for card in dealer_hand:
                index+=1
                if card==11:
                    dealer_hand[index]=1
    if win_check(dealer_hand_total):
        print("Is a draw")
        bank_total+=bet_ammount
    else:
        print("You Win")
        bank_total+=bet_ammount*2

while continue_playing:
    refresh()
    print("Welcome to BlackJack!")
    print("Shuffling...")
    print("Bank: $"+str(bank_total))
    betStart()
    dealer_hand=[]
    player_hand=[]
    dealer_hand_total=0
    player_hand_total=0
    round=1
    flag=True
    index=-1
   
    while continue_hand:

        for cards in range(1,round+2):
            # dealer_hand.append(random_deal())
            # player_hand.append(random_deal())
            dealer_hand_total += dealer_hand[round-1]
            player_hand_total += player_hand[round-1] 
            round+= 1 
            if ace_check_when_losing(player_hand):
                player_hand_total-=10
                for card in player_hand:
                    index+=1
                    if card==11:
                        player_hand[index]=1
            if ace_check_when_losing(dealer_hand):
                dealer_hand_total-=10
                for card in dealer_hand:
                    index+=1
                    if card==11:
                        dealer_hand[index]=1

        if win_check(player_hand_total):
            continue_hand=False
            computer_auto()
        elif player_hand_total<21:
            while player_hand_total<21 and continue_hand==True:
                continue_hand_raw=input("Hit or Stand?: ").lower
        
                if continue_hand_raw=="stand":
                    continue_hand=False
                elif continue_hand_raw=="hit":
                    player_hand.append(random_deal())
                    player_hand_total += player_hand[round-1] 
                    round+= 1 
                    if ace_check_when_losing(player_hand):
                        player_hand_total-=10
                        for card in player_hand:
                            index+=1
                            if card==11:
                                player_hand[index]=1
            if win_check(player_hand_total):
                continue_hand=False
                computer_auto()
            else:
                print("You lose")
                
                
        





