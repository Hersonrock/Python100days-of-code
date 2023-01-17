
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.config(padx=100,pady=50)
window.title("Pomodoro")


#-----------Canvas creation--------------------------------
canvas= Canvas(width=202,height=223)   #Matching image dimentions.Any other dimention will crop the image 
tomato_img=PhotoImage(file="Day28_Pomodoro\\tomato.png") #This is a special object used by canvas.
canvas.create_image(103,112, image=tomato_img)  # This coordinates depict the center of the image.
canvas.grid(column=0,row=0)
#/--------------------------------------------------------





window.mainloop()