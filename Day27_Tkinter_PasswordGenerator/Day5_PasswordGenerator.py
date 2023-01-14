#Password Generator Project
from tkinter import *
import random

window = Tk()
window.title("Password Generator")
window.minsize(width=800,height=600)

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def build_pass(nr_letters,nr_symbols,nr_numbers):
    totalCharacters= range(1,nr_letters+nr_symbols+nr_numbers+1)
    password = []
    print(f"totalCharacters= {len(totalCharacters)}")
    for character in totalCharacters:
        appended=False
        while appended==False:
            print(f"{character}")
            randomChoice= random.randint(1,3)
            if randomChoice==1 and nr_letters>0:
                password.append(LETTERS[random.randint(0,len(LETTERS)-1)])
                nr_letters -= 1
                appended=True
            if randomChoice==2 and nr_symbols>0:
                password.append(SYMBOLS[random.randint(0,len(SYMBOLS)-1)])
                nr_symbols -= 1
                appended=True
            if randomChoice==3 and nr_numbers>0:
                password.append(NUMBERS[random.randint(0,len(NUMBERS)-1)])
                nr_numbers -= 1
                appended=True
    return password

def print_password():
    password=build_pass(nr_letters,nr_symbols,nr_numbers)
    print("Your password is: "+"".join(password))


# print("Welcome to the PyPassword Generator!")
welcome=Label(text="Welcome to the PyPassword Generator!", font=("Arial",15,))
welcome.grid(column=0,row=0)
welcome.config(padx=20,pady=20)


# nr_letters= int(input("How many letters would you like in your password?\n")) 
letter_label=Label(text="How many letters would you like in your password?",font=("Arial",10))
letter_label.grid(column=0,row=1)
letter_label.config(padx=20,pady=20)
letter_entry=Entry(width=20)
letter_entry.insert(END,string=len(LETTERS))
letter_entry.grid(column=0,row=2)
nr_letters=int(letter_entry.get())


nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


print_pass_btn=Button(text="Print Password",command=print_password)
print_pass_btn.grid(column=1,row=0)


window.mainloop()