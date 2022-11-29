# ---------------Turtle-----------------------
# from turtle import Turtle,Screen
# lechuga= Turtle()
# print(lechuga)
# lechuga.shape("turtle")
# lechuga.color("DarkOrchid4")


# lechuga.forward(100)

# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# ---------------Pretty Table-----------------------
# Installed pip with
# python -m pip install -U prettytable
# 

from prettytable import PrettyTable 

table=PrettyTable()


table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align= "l"
print(table)