#Password Generator Project
from tkinter import *
import random

window = Tk()
window.title("Password Generator")
window.minsize(width=500,height=300)

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def build_pass(nr_letters,nr_symbols,nr_numbers):
    totalCharacters= range(1,nr_letters+nr_symbols+nr_numbers+1)
    password = []
    for character in totalCharacters:
        appended=False
        while appended==False:
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
    #Gathering entry content
    nr_letters=int(letter_entry.get())
    nr_symbols =int(symbols_entry.get())
    nr_numbers = int(numbers_entry.get())
    #Building password out of content choosen and printing as a label.
    password="".join(build_pass(nr_letters,nr_symbols,nr_numbers))
    # password_ouput="Your password is: "+"".join(password)
    output_label=Label(text="Your password is:",font=("Arial",10))
    output_label.grid(column=0,row=7,sticky="w")
    output=Entry(width=100)
    output.insert(END,string=password)
    output.grid(column=0,row=8,sticky="w")


# print("Welcome to the PyPassword Generator!")
welcome=Label(text="Welcome to the PyPassword Generator!", font=("Arial",15,))
welcome.grid(column=0,row=0)
welcome.config(padx=20,pady=20)

# Changing console input to Label+Entry
# nr_letters= int(input("How many letters would you like in your password?\n")) 
letter_label=Label(text="How many letters would you like in your password?",font=("Arial",10))
letter_label.grid(column=0,row=1,sticky="w")
letter_label.config(padx=5,pady=5)
letter_entry=Entry(width=5)
letter_entry.insert(END,string=len(LETTERS))
letter_entry.grid(column=0,row=2,sticky="w",padx=30)

# Changing console input to Label+Entry
# nr_symbols = int(input(f"How many symbols would you like?\n"))
symbols_label=Label(text="How many symbols would you like?", font=("Arial",10))
symbols_label.grid(column=0,row=3,sticky="w")
symbols_label.config(padx=5,pady=5)
symbols_entry=Entry(width=5)
symbols_entry.insert(END,string=len(SYMBOLS))
symbols_entry.grid(column=0,row=4,sticky="w",padx=30)

# Changing console input to Label+Entry
#nr_numbers = int(input(f"How many numbers would you like?\n"))
numbers_label=Label(text="How many numbers would you like?",font=("Arial",10))
numbers_label.grid(column=0,row=5,sticky="w")
numbers_label.config(padx=5,pady=5)
numbers_entry=Entry(width=5)
numbers_entry.insert(END,string=len(NUMBERS))
numbers_entry.grid(column=0,row=6,sticky="w",padx=30)

#Definining Button and function
print_pass_btn=Button(text="Print Password",command=print_password)
print_pass_btn.grid(column=1,row=0)


window.mainloop()