from tkinter import *

window = Tk()
window.title("Tkinter window")
window.minsize(width=800,height=600)


#-----To create a label
my_label=Label(text="Label", font=("Arial",24,"bold"))
my_label.pack()  # "Packer" this is needed for the label to display



#------To create an input form

def print_input():
    print(input.get())

input=Entry(width=50)
input.pack()

#----To create a Button

button=Button(text="Click on me", command=print_input)
button.pack()

#----------This should be at the end of program.
window.mainloop()







#-------------------CONTENT-----------------
# # unlimited postional argument
# def sum(*args):
#     sum=0
#     for n in args:
#         sum += n
#     return sum

# print(sum(3,4,5,6,2,1))


# #keyword argument

# def calculate(**kwargs):
#     print(kwargs) #this will print a dictionary

# calculate(add=4,multiply=9)

# #class example for kwarg

# class Car:

#     def __init__(self,**kwarg):

#         #This code will not work if the below is used, .get() must be used instead so the arguments are trully optional.
#         # self.model=kwarg["model"]
#         # self.year=kwarg["year"]
#         self.model=kwarg.get("model")
#         self.year=kwarg.get("year")
 
# spiner=Car(model="spiner")

# print(f"model ={spiner.model},year={spiner.year}") #It returns "None" for year, thanks to .get().
