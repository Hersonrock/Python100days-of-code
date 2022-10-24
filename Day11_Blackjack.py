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

from ctypes import sizeof
import os
import random
from tkinter import N

#HINT: Clearing the Screen
#   os.system('cls')

bank_total=1000
continue_playing=True
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
    continue_playing_raw=""
    while continue_playing_raw!="y" and continue_playing_raw!="n":
        continue_playing_raw=input("Do you want to continue playing? (y/n): ").lower()
        if continue_playing_raw=="y":
            return True
        elif continue_playing_raw=="n":
            return False
        else:    
            print("Invalid Option")
    continue_playing_raw=""

def random_deal():
    first_deal= random.randint(0,11)
    return cards[first_deal]

def ace_check(hand):

    index=-1
    if sumHand(hand)>21:
        for card in hand:
            index += 1
            if card ==11:
                return index
            else:
                return -1
    else:
        return -1

def  sumHand(hand):

    sum=0
    for card in hand:
        sum +=card
    return sum

# def check21(hand):

#     if sumHand(hand)==21:
#         return True

# def under21(hand):

#     if sumHand(hand)<21:
#         return True

# def over21(hand):

#     if sumHand(hand)>21:
#         return True

def hit():

    askForCard=None
   
    while askForCard==None:
        answer= input("Hit or Stand?: ").lower()
        if answer=="hit":
            askForCard=True
        elif answer=="stand":
            askForCard=False
        else:
            print("Incorrect option, try again")

    return askForCard

# def  printHand(hand,isPlayer,isFristRound):

#     for i in range(0,len(hand)):
#         if i==0:
#             if isPlayer:
#                 print(f"Player Hand: {hand[i]},",end="")
#             else:
#                 print(f"Dealer Hand: {hand[i]},",end="")
#         elif i==len(hand)-1:
#             if isPlayer:
#                 print(f"{hand[i]} = {sumHand(hand)}")
#             elif isFristRound:
#                 print("X")
#             else:
#                 print(f"{hand[i]} = {sumHand(hand)}")
#         else:
#             print(f"{hand[i]},",end="")

while continue_playing:
    refresh()
    print("Welcome to BlackJack!")
    print("Shuffling...")
    print("Bank: $"+str(bank_total))
    bank_total= betStart()

    dealerHand=[]
    playerHand=[]


    #Computer and player first deal
    for i in range(0,2):
        dealerHand.append(random_deal())
        playerHand.append(random_deal())
        

    if ace_check(dealerHand)!=-1:
        dealerHand[ace_check(dealerHand)]=1
    if ace_check(playerHand)!=-1:
        playerHand[ace_check(playerHand)]=1    
    
    # printHand(dealerHand,False,True)
    # printHand(playerHand,True,True)
    print(f"Dealer Hand: {dealerHand[0]},{dealerHand[1]}")
    print(f"Player Hand: {playerHand[0]},{playerHand[1]}")
    
    if check21(dealerHand) or check21(playerHand):
        if check21(dealerHand) and check21(playerHand):
            print("Is a Tie")
        elif check21(dealerHand):
            print("You Lose")
        elif check21(playerHand):
            print("You Win")

    # if not hit():
    #     while sumHand(dealerHand)<sumHand(playerHand) and under21(dealerHand):
    #         dealerHand.append(random_deal())
    #         if ace_check(dealerHand)!=-1:
    #             dealerHand[ace_check(dealerHand)]=1
    #     printHand(dealerHand,False,False)
    #     if over21(dealerHand):
    #         print("You Win")
    #     elif check21(dealerHand) or sumHand(dealerHand)>sumHand(playerHand):
    #         print("You Lose")
    
    continue_playing=continue_playing_function()
