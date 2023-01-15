from tkinter import *

FONT=("Arial",10)

window= Tk()
window.title("Miles to KM converter")
window.minsize(width=400,height=300)

def to_km():

    result_label2.delete(0,END)
    miles=int(entry_label1.get())
    result_label2.insert(END,string=f"{round(miles/1.6,2)}")
    

label_main= Label(text="Miles to Km converter",font=("Arial",20))
label_main.grid(column=0,row=0,sticky="n",padx=10,pady=10)

label1=Label(text="Input miles:",font=FONT)
label1.grid(column=0,row=1,padx=10,pady=10,sticky="w")
entry_label1=Entry(width=10)
entry_label1.grid(column=0,row=2,sticky="w",padx=20,pady=10)

button=Button(text="Convert",command=to_km)
button.grid(column=0,row=3,padx=10,pady=10,sticky="w")

label2=Label(text="Converted to miles:",font=FONT)
label2.grid(column=0,row=4,sticky="w",padx=10,pady=10)

result_label2=Entry(width=10)
result_label2.grid(column=0,row=5,sticky="w",padx=20,pady=10)


window.mainloop()
