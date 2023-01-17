
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

def reset():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
    pass
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.config(padx=100,pady=10,bg=YELLOW)
window.title("Pomodoro")

# ---------------------------- CANVAS------------------------------- #
canvas= Canvas(width=200,height=300,bg=YELLOW, highlightthickness=0)   #Matching image dimentions.Any other dimention will crop the image 
tomato_img=PhotoImage(file="Day28_Pomodoro\\tomato.png") #This is a special object used by canvas.
canvas.create_image(100,130, image=tomato_img)  # This coordinates depict the center of the image.
canvas.grid(column=1,row=2)
canvas.create_text(100,160, text="00:00",fill="white", font=(FONT_NAME,35,"bold"))

timer_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,38),bg=YELLOW)
timer_label.grid(column=1,row=1)

checkmark_label=Label(text="✔",fg=GREEN,font=(FONT_NAME,15,"bold"),bg=YELLOW)
checkmark_label.grid(column=1,row=3)


# canvas.create_text(100,30, text="Timer",fill=GREEN,font=(FONT_NAME,38,"bold"))
# canvas.create_text(100,320, text="✔",fill=GREEN,font=(FONT_NAME,15,"bold"))

# ---------------------------- Button ------------------------------- #

start=Button(text="Start",command=start,highlightthickness=0)
start.grid(column=0,row=3,sticky="w")
reset=Button(text="Reset",command=reset,highlightthickness=0)
reset.grid(column=2,row=3,sticky="e")




window.mainloop()