from turtle import Turtle,Screen
import random

size=200
circle_ammount=50


#Basic start, a turtle and a screen that does not close inmediately.
screen = Screen()
screen.colormode(255)
lechuga = Turtle()
lechuga.shape("turtle")
lechuga.speed(0)
lechuga.pensize(2)


for n in range (1,circle_ammount+1):
    lechuga.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    lechuga.circle(size)
    lechuga.right(360/circle_ammount)


screen.screensize(600,800)
screen.exitonclick()
