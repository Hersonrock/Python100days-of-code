from turtle import Turtle
from scoreboard import SCREEN_HEIGHT,SCREEN_WIDTH
import random


HEADING_CHANGE=50

UP= 90
DOWN=270
LEFT=180
RIGHT=0

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.setheading(RIGHT)
        self.p1loss=0
        self.p2loss=0
        
    def move(self,speed):
        self.forward(speed)
            

    def bounce(self,touch,heading):

        clockwise=heading-90
        counterclock=heading+90
        #Avoids perfect bounces, These should be practically impossible while on game.
        if heading==UP or heading==DOWN or heading==LEFT or heading==RIGHT:
            self.setheading(heading+random.randrange(-HEADING_CHANGE,HEADING_CHANGE,HEADING_CHANGE)+180)
        
        elif(heading>0 and heading<90):
            if touch=="top":
                self.setheading(clockwise)
            if touch=="right":
                self.setheading(counterclock)
        elif(heading>90 and heading<180):
            if touch=="top":
                self.setheading(counterclock)
            if touch=="left":
                self.setheading(clockwise)
        elif(heading>180 and heading<270):
            if touch=="bot":
                self.setheading(clockwise)
            if touch=="left":
                self.setheading(counterclock)
        elif(heading>270 and heading<360):
            if touch=="bot":
                self.setheading(counterclock)
            if touch=="right":
                self.setheading(clockwise)
             
        print(self.heading())

    def collision(self):

        if self.position()[0]>(SCREEN_WIDTH/2):
            # self.color("red")
            # self.touch="right"
            # self.bounce(self.touch,self.heading())
            self.p2loss+=1
            self.home()
            self.setheading(LEFT)
        if self.position()[0]<-(SCREEN_WIDTH/2):
            # self.color("blue")
            # self.touch="left"
            # self.bounce(self.touch,self.heading())
            self.p1loss+=1
            self.home()
            self.setheading(RIGHT)
        if self.position()[1]>(SCREEN_HEIGHT/2)-10:
            self.color("green")
            self.touch="top"
            self.bounce(self.touch,self.heading())
        if self.position()[1]<-(SCREEN_HEIGHT/2)+10:
            self.color("yellow")
            self.touch="bot"
            self.bounce(self.touch,self.heading())
            
    def paddle_bounce(self,paddle):
        if paddle=="p1":
            self.color("red")
            self.touch="left"
            self.bounce(self.touch,self.heading())
        if paddle=="p2":
            self.color("blue")
            self.touch="right"
            self.bounce(self.touch,self.heading())


    
