from tkinter import *
from PasswordGenerator import password_gen

LETTER=4
SYMBOLS=4
NUMBERS=4
password=""


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    global password
    password_entry.delete(0, END)
    password=password_gen(LETTER,SYMBOLS,NUMBERS)
    password_entry.insert(END,string=password)
   
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_to_file():

    webpage= website_entry.get()
    username= email_entry.get()

    entry="".join(f"{webpage} | {username} | {password}\n")

    score_file = open("Day29_PasswordManager\database.txt",mode="a")
    score_file.write(entry)
    score_file.close()


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="white")
canvas=Canvas(width=200,height=200,bg="white",highlightthickness=0)

logo_img=PhotoImage(file="Day29_PasswordManager\\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

#row 1
website_label=Label(text="Website:",bg="white")
website_label.grid(column=0,row=1,sticky="e")

website_entry=Entry(width=32)
website_entry.grid(column=1,row=1,columnspan=2,sticky="w")
website_entry.focus()

#row 2
email_label=Label(text="Email/Username:",bg="white")
email_label.grid(column=0,row=2,sticky="e")

email_entry=Entry(width=32)
email_entry.grid(column=1,row=2,columnspan=2,sticky="w")

#row 3
password_label=Label(text="Password:",bg="white")
password_label.grid(column=0,row=3,sticky="e")

password_btn=Button(text="Generate Password",command=generate_pass)
password_btn.grid(column=2,row=3,columnspan=2)

password_entry=Entry(width=32)
password_entry.grid(column=1,row=3,sticky="w")

#row 4
add_btn=Button(text="Add",command=add_to_file,width=43)
add_btn.grid(column=1,row=4,columnspan=2)



window.mainloop()