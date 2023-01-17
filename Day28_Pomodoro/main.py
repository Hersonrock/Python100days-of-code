
from tkinter import *
import math

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

def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    minutes=5
    seconds= minutes*60
    count_down(seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):


    #Solution using ceil? Looks more complicated.
    # minutes_div=count/60
    # if minutes_div<1:
    #     minutes=0
    # else:
    #     minutes=int(math.ceil(minutes_div))
    # seconds=int(math.ceil(count%60))


    minutes=math.floor(count/60)
    seconds=count%60


    if minutes<10:
        if seconds<10:
            display_text="0"+str(minutes)+":0"+str(seconds)
        if seconds>=10:
            display_text="0"+str(minutes)+":"+str(seconds)
    elif minutes>=10:
        if seconds<10:
            display_text=str(minutes)+":0"+str(seconds)
        if seconds>=10:
            display_text=str(minutes)+":"+str(seconds)


    canvas.itemconfig(timer_text,text=display_text)

    if count>0:
        window.after(1000,count_down,count-1)
        print(f"minutes= {minutes}")
        print(f"seconds= {seconds}")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.config(padx=100,pady=10,bg=YELLOW)
window.title("Pomodoro")



# ---------------------------- CANVAS------------------------------- #
canvas= Canvas(width=200,height=300,bg=YELLOW, highlightthickness=0)   #Matching image dimentions.Any other dimention will crop the image 
tomato_img=PhotoImage(file="Day28_Pomodoro\\tomato.png") #This is a special object used by canvas.
canvas.create_image(100,130, image=tomato_img)  # This coordinates depict the center of the image.
canvas.grid(column=1,row=2)

timer_text = canvas.create_text(100,160, text="00:00",fill="white", font=(FONT_NAME,35,"bold"))




timer_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,38),bg=YELLOW)
timer_label.grid(column=1,row=1)

checkmark_label=Label(text="✔",fg=GREEN,font=(FONT_NAME,15,"bold"),bg=YELLOW)
checkmark_label.grid(column=1,row=3)


# canvas.create_text(100,30, text="Timer",fill=GREEN,font=(FONT_NAME,38,"bold"))
# canvas.create_text(100,320, text="✔",fill=GREEN,font=(FONT_NAME,15,"bold"))

# ---------------------------- Button ------------------------------- #

start_timer=Button(text="Start",command=start_timer,highlightthickness=0)
start_timer.grid(column=0,row=3,sticky="w")
reset_timer=Button(text="Reset",command=reset_timer,highlightthickness=0)
reset_timer.grid(column=2,row=3,sticky="e")




window.mainloop()