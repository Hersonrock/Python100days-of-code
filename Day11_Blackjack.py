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
cards=[11,2,3,4,5,6,7,8,9,10,10,10]

def refresh():
    """refreshes console"""
    os.system('cls')
    print(logo)

def bet_start():
    """asks for the player initial bet ammount and returns bank remaining ammount"""
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
    """checks if the player wants to continue playing"""
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
    """deals a random card from the cards list"""
    first_deal= random.randint(0,11)
    return cards[first_deal]

def ace_check(hand):
    """Returns ace index if there is an ace on the hand AND if the hand sum goes over 21, returns -1 when nothing is found"""
    index=-1
    if sum(hand)>21:
        for card in hand:
            index += 1
            if card ==11:
                return index
            else:
                return -1
    else:
        return -1

def check_21(hand):

    if sum(hand)==21:
        return True

def under_21(hand):

    if sum(hand)<21:
        return True

def over_21(hand):

    if sum(hand)>21:
        return True

def hit():
    """checks if the player wants an extra card \"hit\" or not \"stand\" """
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

def print_hand(hand,isPlayer,isFirstRound):
    """Function will print based on the list Hand, if the print if for a player and if it is the first round or not"""
    for i in range(0,len(hand)):
        if i==0:
            if isPlayer:
                print(f"Player Hand: {hand[i]},",end="")
            else:
                print(f"Dealer Hand: {hand[i]},",end="")
        elif i==len(hand)-1:
            if isPlayer:
                print(f"{hand[i]} = {sum(hand)}")
            elif isFirstRound:
                print("X")
            else:
                print(f"{hand[i]} = {sum(hand)}")
        else:
            print(f"{hand[i]},",end="")

while continue_playing:
    refresh()
    print("Welcome to BlackJack!")
    print("Shuffling...")
    print("Bank: $"+str(bank_total))

    #Initializing variables
    bet_total= bank_total-bet_start()
    bank_total -= bet_total
    bet_multiplier=2
    dealerHand=[]
    playerHand=[]
    playerWon=-2

    #Computer and player first deal
    for i in range(0,2):
        dealerHand.append(random_deal())
        playerHand.append(random_deal())
    if ace_check(dealerHand)!=-1:
        dealerHand[ace_check(dealerHand)]=1
    if ace_check(playerHand)!=-1:
        playerHand[ace_check(playerHand)]=1    
    print_hand(dealerHand,False,True)
    print_hand(playerHand,True,True)

    #Natural Win initial check, a winner can be defined here by the first deal.
    if check_21(dealerHand) or check_21(playerHand):
        if check_21(dealerHand) and check_21(playerHand):
            print("Is a Tie")
            playerWon=-1
        elif check_21(dealerHand):
            print("You Lose")
            playerWon=0
        elif check_21(playerHand):
            print("You Win")
            playerWon=1
            bank_total+=bet_total*bet_multiplier
            print("Bank: $"+str(bank_total))
    #Game CoreLoop ; player -2=None, -1=Tie, 0=Loss, 1=Win
    while playerWon==-2:
        #If the player wants to stay with current hand , computer will loop untill game is outcome is defined.
        if not hit():
            while sum(dealerHand)<=sum(playerHand) and under_21(dealerHand):
                dealerHand.append(random_deal())
                if ace_check(dealerHand)!=-1:
                    dealerHand[ace_check(dealerHand)]=1
            print_hand(dealerHand,False,False)
            if over_21(dealerHand):
                print("You Win")
                playerWon=1
                bank_total+=bet_total*bet_multiplier
                print("Bank: $"+str(bank_total))
            elif check_21(dealerHand) or sum(dealerHand)>sum(playerHand):
                print("You Lose")
                playerWon=0
        #If player wants another hand, a random card is appended and win conditions are checked, until player wins, losses or asks for another card.
        else:
            playerHand.append(random_deal())
            if ace_check(playerHand)!=-1:
                playerHand[ace_check(playerHand)]=1
            print_hand(playerHand,True,False)
            if over_21(playerHand):
                print("You Lose")
                playerWon=0
            elif check_21(playerHand):
                print("You Win")
                playerWon=1
                bank_total+=bet_total*bet_multiplier
                print("Bank: $"+str(bank_total))

# main loop is reset if the player wants, player keeps current money, or is reset to initial ammount in case it reaches $0
    if bank_total>0:
        continue_playing=continue_playing_function()
    else:
        bank_total=1500
        continue_playing=continue_playing_function()