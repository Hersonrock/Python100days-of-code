from turtle import Turtle,Screen
import random
import colorgram

total_dot=25
color_number=10
step=30
startx=-400
starty=-300

colors= colorgram.extract("E:\Python 100 days\Day18_TurtleChallenge\megaman.jpg",color_number)

#Basic start, a turtle and a screen that does not close inmediately.
screen = Screen()
screen.colormode(255)
lechuga = Turtle()
lechuga.shape("turtle")
lechuga.speed(0)
lechuga.pensize(2)
lechuga.penup()
lechuga.pendown()

for i in range (0,total_dot+1):
    
    for j in range(0,total_dot+1):
        x=startx+(i*step)
        y=starty+(j*step)

        rand_color=random.randint(0,color_number-1)
        lechuga.penup()
        lechuga.setpos(x,y)
        lechuga.pendown()
        lechuga.dot(step/2, colors[rand_color].rgb)
   

screen.screensize(800,600)
screen.exitonclick()
