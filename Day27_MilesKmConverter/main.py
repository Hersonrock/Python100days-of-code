from tkinter import *

FONT=("Arial",10)

window= Tk()
window.title("Miles to KM converter")
window.minsize(width=400,height=300)


label_main= Label(text="Miles to Km converter",font=("Arial",20))
label_main.grid(column=0,row=0,sticky="n",padx=10,pady=10)




window.mainloop()
