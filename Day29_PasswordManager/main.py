from tkinter import *
from tkinter import messagebox
from PasswordGenerator import password_gen
import pyperclip
import json

LETTER=4
SYMBOLS=4
NUMBERS=4


#--------------------------------SEARCH-------------------------------------------#

def search():
    website=website_entry.get()
    try:
        database_file = open("Day29_PasswordManager\database.json",mode="r")
    except FileNotFoundError:
        messagebox.showwarning(title="Warning",message="There are no saved passwords")
    else:
        data=json.load(database_file)
        database_file.close()
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        if website in data:
            username=data[website]["username"]
            password=data[website]["password"]

            email_entry.insert(0,string=username)
            password_entry.insert(0,string=password)
            write_label("Website Found")
        else:
            write_label("No entry for Website...")

                


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    password=""
    password_entry.delete(0, END)
    password=password_gen(LETTER,SYMBOLS,NUMBERS)
    password_entry.insert(END,string=password)
    pyperclip.copy(password)
    write_label("Copied to Clipboard...")
   
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_to_file():

    webpage= website_entry.get()
    username= email_entry.get()
    password= password_entry.get()
    new_data={
        webpage:{
            "username":username,
            "password":password
        }
    }

    if len(webpage)*len(username)*len(password)==0:
        messagebox.showwarning(title="Warning",message="Please complete the fields.")
    else:

        is_ok=messagebox.askokcancel(title="Save to file",message=f"Webpage:\t{webpage}\nUsername/Email:\t{username}\nPassword:\t{password}\nPress OK to continue... ")
        if is_ok:
            try:
                #Opening file
                database_file = open("Day29_PasswordManager\database.json",mode="r")
                data=json.load(database_file)
            except FileNotFoundError:
                database_file = open("Day29_PasswordManager\database.json",mode="w")
                json.dump(new_data,database_file,indent=4)
            else:
                #Updating Data
                data.update(new_data)

            #Saving updated data
            database_file.close()
            database_file = open("Day29_PasswordManager\database.json",mode="w")
            json.dump(data,database_file,indent=4)
            database_file.close()
            password_entry.delete(0, END)
            write_label("Password saved")
            

def write_label(entry):
    output_label.config(text=entry)



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

website_search_btn=Button(text="Search",command=search,width=14)
website_search_btn.grid(column=2,row=1,columnspan=2)

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


#row 5
output_label=Label(text="",bg="white")
output_label.grid(column=1,row=5,sticky="w")




window.mainloop()