from turtle import Turtle,Screen
import random


screen_width=500
screen_height=400
screen_floor=-screen_height/2
turtles=[]
color=['blue','cyan','DarkRed','chartreuse','DarkOrange']
screen=Screen()
screen.setup(screen_width+50,screen_height+50)
base_movement=10

Leonardo=Turtle()
Donatello=Turtle()
Raphael=Turtle()
Michelangelo=Turtle()
Randy=Turtle()
turtles.append(Leonardo)
turtles.append(Donatello)
turtles.append(Raphael)
turtles.append(Michelangelo)
turtles.append(Randy)



def has_won(turtle):
    if turtle.position()[0]> ((screen_width/2)-50):
        return True
    else:
        return False

def initiate_turtle():
    i=0
    for turtle in turtles:
        i+=1
        spacing=screen_height/len(turtles)+1
        turtle.penup()
        turtle.setpos(-screen_width/2,screen_floor+spacing*(i-1/2))
        turtle.color(color[i-1])
        turtle.shape("turtle")
        turtle.pendown()

def move_turtle(turtle):
    rand_step=random.randint(0,10)
    turtle.forward(base_movement+rand_step)

def win_check():

    global wining_turtle 
    wining_turtle=""
    for turtle in turtles:
        if has_won(turtle)==True:
            wining_turtle=turtle.color()[0]
            return True
    return False

initiate_turtle()

while win_check()==False:
    for turtle in turtles:
        move_turtle(turtle)




print(f"Winner is {wining_turtle}")

screen.exitonclick()