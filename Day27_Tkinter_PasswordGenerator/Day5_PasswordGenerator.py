#Password Generator Project
from tkinter import *
import random

window = Tk()
window.title("Password Generator")
window.minsize(width=600,height=300)

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
ENTRY_PAD=30
LABEL_PAD=5
BASE_FONT=("Arial",10)

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

    #Building password
    password="".join(build_pass(nr_letters,nr_symbols,nr_numbers))

    #Configuring output Label and entry
    output_label=Label(text="Your password is:",font=BASE_FONT)
    output_label.grid(column=0,row=8,sticky="w",padx=LABEL_PAD)
    output=Entry(width=85)
    output.insert(END,string=password)
    output.grid(column=0,row=9,sticky="w",padx=ENTRY_PAD)

    #Changes button text
    print_pass_btn.config(text="Regenerate")



# print("Welcome to the PyPassword Generator!")
welcome=Label(text="Welcome to the PyPassword Generator!", font=("Arial",15,))
welcome.grid(column=0,row=0,sticky="n")
welcome.config(padx=20,pady=20)

# Changing console input to Label+Entry
# nr_letters= int(input("How many letters would you like in your password?\n")) 
letter_label=Label(text="How many letters would you like in your password?",font=BASE_FONT)
letter_label.grid(column=0,row=1,sticky="w")
letter_label.config(padx=LABEL_PAD,pady=LABEL_PAD)
letter_entry=Entry(width=5)
letter_entry.insert(END,string=len(LETTERS))
letter_entry.grid(column=0,row=2,sticky="w",padx=ENTRY_PAD)

# Changing console input to Label+Entry
# nr_symbols = int(input(f"How many symbols would you like?\n"))
symbols_label=Label(text="How many symbols would you like?", font=BASE_FONT)
symbols_label.grid(column=0,row=3,sticky="w")
symbols_label.config(padx=LABEL_PAD,pady=LABEL_PAD)
symbols_entry=Entry(width=5)
symbols_entry.insert(END,string=len(SYMBOLS))
symbols_entry.grid(column=0,row=4,sticky="w",padx=ENTRY_PAD)

# Changing console input to Label+Entry
#nr_numbers = int(input(f"How many numbers would you like?\n"))
numbers_label=Label(text="How many numbers would you like?",font=BASE_FONT)
numbers_label.grid(column=0,row=5,sticky="w")
numbers_label.config(padx=LABEL_PAD,pady=LABEL_PAD)
numbers_entry=Entry(width=5)
numbers_entry.insert(END,string=len(NUMBERS))
numbers_entry.grid(column=0,row=6,sticky="w",padx=ENTRY_PAD)

#Definining Button and function
print_pass_btn=Button(text="Print Password",command=print_password)
print_pass_btn.grid(column=0,row=7,sticky="n")


window.mainloop()