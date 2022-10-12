print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice=input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\": ").lower()
if choice =="left":
    choice=input("You find a very shallow river, it does not seem very dangerous. What do you want to do? Type \"swim\" or \"jump over it\": ").lower()
    if choice == "jump over it":
        choice=input("It was a bigger jump than expected you barely made it, on the other side you see three doors. Which one to open? Type \"left\", \"right\" or \"center\": ").lower()
        if choice=="left":
            print("The room appears empty, you go in to check further but you fall to a pit with snakes.  \nGame Over.")
        elif choice=="right":
            print("You hear a mechanic clank and a trap triggers, you get hit by a poisoned dart.  \nGame Over.")
        elif choice=="center":
            print("You see a shiny treasure full of gems and gold, is all yours \nYou Win")
        else:
            print("You failed to choose, a beast appeared out of dark and ate you \nGame Over.")
    elif choice == "swim":
        print("Attacked by trout \nGame Over.")
    else:
        print("You failed to choose correctly and slip hitting your head on a rock \nGame Over.")

else:
    print("You Fall into a hole. \nGame Over.")


