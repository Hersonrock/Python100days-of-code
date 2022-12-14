#Password Generator Project
from ast import While
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
##########GOING FOR THE HARD LEVEL##########

password = []
appended = False
totalCharacters= range(1,nr_letters+nr_symbols+nr_numbers+1)

for character in totalCharacters:
    appended=False
    while appended==False:
        randomChoice= random.randint(1,3)
        if randomChoice==1 and nr_letters>0:
            password.append(letters[random.randint(0,len(letters)-1)])
            nr_letters -= 1
            appended=True
        if randomChoice==2 and nr_symbols>0:
            password.append(symbols[random.randint(0,len(symbols)-1)])
            nr_symbols -= 1
            appended=True
        if randomChoice==3 and nr_numbers>0:
            password.append(numbers[random.randint(0,len(numbers)-1)])
            nr_numbers -= 1
            appended=True

print("Your password is: "+"".join(password))