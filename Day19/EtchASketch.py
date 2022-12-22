from turtle import Turtle,Screen
timmy=Turtle()
screen= Screen()
timmy.shape("turtle")


def move_forwards():
    timmy.forward (10)
def move_backwards():
    timmy.backward(10)
# def turn_right():
#     timmy.right (10)
#     timmy.forward (10)
# def turn_left():
#     timmy.left (10)
#     timmy.forward (10)

def turn_right():
    new_heading=timmy.heading()+10
    timmy.seth(new_heading)
def turn_left():
    new_heading=timmy.heading()-10
    timmy.seth(new_heading)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()