import tkinter


window = tkinter.Tk()
window.title("Tkinter window")
window.minsize(width=800,height=600)


#-----To create a label
my_label=tkinter.Label(text="Label", font=("Arial",24,"bold"))
my_label.pack()  # "Packer" this is needed for the label to display


#----------This should be at the end of program.
window.mainloop()