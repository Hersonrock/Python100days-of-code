rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

playerInput = int(input("Choose, Type 0 for Rock, Type 1 for Paper or 2 for Scissors: "))
computerInput= random.randint(0,2)

#Need to make this more efficient.
if playerInput ==0:
    if computerInput == 0:
        print("You Choose \n"+rock+"\nComputer Choose"+rock)
        print("It's a draw")
    elif computerInput == 1:
        print("You Choose \n"+rock+"\nComputer Choose"+paper)
        print("You Lose")
    else:
        print("You Choose \n"+rock+"\nComputer Choose"+scissors)
        print("You Win")
elif playerInput ==1:
    if computerInput == 0:
        print("You Choose \n"+paper+"\nComputer Choose"+rock)
        print("You Win")
    elif computerInput == 1:
        print("You Choose \n"+paper+"\nComputer Choose"+paper)
        print("It's a draw")
    else:
        print("You Choose \n"+paper+"\nComputer Choose"+scissors)
        print("You Lose")
elif playerInput ==2:
    if computerInput == 0:
        print("You Choose \n"+scissors+"\nComputer Choose"+rock)
        print("You Lose")
    elif computerInput == 1:
        print("You Choose \n"+scissors+"\nComputer Choose"+paper)
        print("You Win")
    else:
        print("You Choose \n"+scissors+"\nComputer Choose"+scissors)
        print("It's a draw")

