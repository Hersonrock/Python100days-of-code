
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


difficulty=None
attempts=0
secret=random.randint(1,100)
guess=0


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def is_in_range(number):
    for i in range(1,101):
        if number == i:
            return True
    return False

while (difficulty==None):
    difficulty_raw=input("Choose a difficulty. Type \'easy\' or \'hard\': ").lower()
    if (difficulty_raw=="easy"):
        difficulty=1
    elif (difficulty_raw=="hard"):
        difficulty=2
    else:
        print("Wrong option")

if difficulty==1:
    attempts=10
elif difficulty==2:
    attempts=5

print(f"The secret number is : {secret}")

while True:
    try:
        guess=int(input("Make a guess: "))
        if is_in_range(guess):
            break
        else:
            print("Number out of range, try again.")
    except:
        print("Please input a number, try again.")

