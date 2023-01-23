from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    pass

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
add_btn=Button(text="Add",command=add,width=43)
add_btn.grid(column=1,row=4,columnspan=2)



window.mainloop()