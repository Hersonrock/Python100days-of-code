
from turtle import Turtle,Screen
import random

side_lenght=90
start_shape=3
end_shape=10


#Basic start, a turtle and a screen that does not close inmediately.
screen = Screen()
screen.colormode(255)
lechuga = Turtle()
lechuga.shape("turtle")
lechuga.speed(0)


lechuga.up()
lechuga.setpos(-side_lenght/2,250)
lechuga.down()


for n in range(start_shape,end_shape+1):
    angle=180*(1-(n-2)/n)
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)

    lechuga.pencolor((r,g,b))
    for i in range(n):
        lechuga.forward(side_lenght)
        lechuga.right(angle)


screen.screensize(600,800)
screen.exitonclick()
