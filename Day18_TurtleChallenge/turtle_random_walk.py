
from turtle import Turtle,Screen
import random

step=50


#Basic start, a turtle and a screen that does not close inmediately.
screen = Screen()
screen.colormode(255)
lechuga = Turtle()
lechuga.shape("turtle")
lechuga.speed(0)
lechuga.pensize(10)


for n in range(1,201):
    lechuga.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    rand_dir=random.randint(0,3)
    
    if rand_dir==0:
        lechuga.forward(step)
    if rand_dir==1:
        lechuga.right(90)
        lechuga.forward(step)
    if rand_dir==2:
        lechuga.left(90)
        lechuga.forward(step)
    if rand_dir==3:
        lechuga.back(step)

screen.screensize(600,800)
screen.exitonclick()
