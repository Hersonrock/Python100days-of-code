
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
reps= 0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps=0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    
    global reps
    reps+=1

    work_sec= WORK_MIN*60
    work_break_sec= SHORT_BREAK_MIN*60
    long_break_sec= LONG_BREAK_MIN*60


    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break",fg=RED)
    if reps%2==0:
        count_down(work_break_sec)
        timer_label.config(text="Short Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    global timer
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
        timer=window.after(1000,count_down,count-1)
    else: 
        start_timer()
        mark=""
        work_sessions= math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark_label.config(text=mark)


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


timer_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,38,"bold"),bg=YELLOW)
timer_label.grid(column=1,row=1)

checkmark_label=Label(text="",fg=GREEN,font=(FONT_NAME,15,"bold"),bg=YELLOW)
checkmark_label.grid(column=1,row=3)


# canvas.create_text(100,30, text="Timer",fill=GREEN,font=(FONT_NAME,38,"bold"))
# canvas.create_text(100,320, text="✔",fill=GREEN,font=(FONT_NAME,15,"bold"))

# ---------------------------- Button ------------------------------- #

start_timer_btn=Button(text="Start",command=start_timer,highlightthickness=0)
start_timer_btn.grid(column=0,row=3,sticky="w")
reset_timer_btn=Button(text="Reset",command=reset_timer,highlightthickness=0)
reset_timer_btn.grid(column=2,row=3,sticky="e")


window.mainloop()