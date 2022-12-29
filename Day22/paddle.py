from turtle import Turtle
from scoreboard import SCREEN_HEIGHT,SCREEN_WIDTH


 
class Paddle():
    def __init__(self,location,number):
        self.segments=[]
        self.build_paddle(location)
        self.add_segement(number)

    def build_paddle(self,location): 
        segment=Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.hideturtle()
        segment.goto(location)
        segment.showturtle()
        self.segments.append(segment)

    def add_segement(self,number):

        for i in range(1,number):
            segment=Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.hideturtle()
            segment.goto(self.segments[0].position()[0],self.segments[i-1].position()[1]-20)
            segment.showturtle()
            self.segments.append(segment)
   