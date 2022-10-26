
from random import random
from tkinter import W
from tkinter.messagebox import NO


logo="""
 _______               ___.                    ________                             
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ ______
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >
        \/            \/    \/     \/                \/            \/     \/     \/
"""

import random


EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
difficulty=None
attempts=0
secret=random.randint(1,100)
guess=0
win=False

#Game Setup
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while (difficulty==None):
    difficulty_raw=input("Choose a difficulty. Type \'easy\' or \'hard\': ").lower()
    if (difficulty_raw=="easy"):
        difficulty=1
    elif (difficulty_raw=="hard"):
        difficulty=2
    else:
        print("Wrong option")

if difficulty==1:
    attempts=EASY_LEVEL_TURNS
elif difficulty==2:
    attempts=HARD_LEVEL_TURNS


#Game CoreLoop
while attempts>0:
    while True:
        #makes sure the input is both a number, and in range 
        try:
            guess=int(input("Make a guess: "))
            attempts -=1
            if guess >=1 and guess<=100:
                
                break
            else:
                print("Number out of range, try again.")
                print(f"Attempts remaining= {attempts}")
        except:
            attempts-=1
            print("Please input a number, try again.")
            print(f"Attempts remaining= {attempts}")
            
#Checks for win condition
    if guess==secret:
        print("Congratulations")
        win=True
        attempts=0
    elif guess<secret:
        print("Too Low")
    else:
        print("Too high")

    print(f"Attempts remaining= {attempts}")

if win:
    print("You win!")
else:
    print("You lose")
