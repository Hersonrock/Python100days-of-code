from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.minsize(width=220,height=220)
window.config(padx=20,pady=20,bg="white")

canvas=Canvas(width=200,height=200,bg="white",highlightthickness=0)

logo_img=PhotoImage(file="Day29_PasswordManager\\logo.png")
canvas.create_image(100,95,image=logo_img)
canvas.grid(column=0,row=0)

window.mainloop()