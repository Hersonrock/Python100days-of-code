# import tkinter

# window = tkinter.Tk()
# window.title("Tkinter window")
# window.minsize(width=800,height=600)


# #-----To create a label
# my_label=tkinter.Label(text="Label", font=("Arial",24,"bold"))
# my_label.pack()  # "Packer" this is needed for the label to display


# #----------This should be at the end of program.
# window.mainloop()

# unlimited postional argument
def sum(*args):
    sum=0
    for n in args:
        sum += n
    return sum

print(sum(3,4,5,6,2,1))


#keyword argument

def calculate(**kwargs):
    print(kwargs) #this will print a dictionary

calculate(add=4,multiply=9)
