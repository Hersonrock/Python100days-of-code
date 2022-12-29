from turtle import Turtle
import random

SCREEN_HEIGHT=600
SCREEN_WIDTH=600
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
        
    def move(self,speed):
        self.forward(speed)
            

    def bounce(self,touch,heading):
        #Avoids perfect bounces, These should be practically impossible while on game.
        if heading==UP or heading==DOWN or heading==LEFT or heading==RIGHT:
            self.setheading(heading+random.randrange(-HEADING_CHANGE,HEADING_CHANGE,HEADING_CHANGE)+180)
        
        elif(heading>0 and heading<90):
            if touch=="top":
                self.setheading(heading-90)
            if touch=="right":
                self.setheading(heading+90)
        elif(heading>90 and heading<180):
            if touch=="top":
                self.setheading(heading+90)
            if touch=="left":
                self.setheading(heading-90)
        elif(heading>180 and heading<270):
            if touch=="bot":
                self.setheading(heading-90)
            if touch=="left":
                self.setheading(heading+90)
        elif(heading>270 and heading<360):
            if touch=="bot":
                self.setheading(heading+90)
            if touch=="right":
                self.setheading(heading-90)
             
        print(self.heading())

    def collision(self):

        if self.position()[0]>(SCREEN_WIDTH/2)-10:
            self.color("red")
            self.touch="right"
            self.bounce(self.touch,self.heading())
        if self.position()[0]<-(SCREEN_WIDTH/2)+10:
            self.color("blue")
            self.touch="left"
            self.bounce(self.touch,self.heading())
        if self.position()[1]>(SCREEN_HEIGHT/2)-10:
            self.color("green")
            self.touch="top"
            self.bounce(self.touch,self.heading())
        if self.position()[1]<-(SCREEN_HEIGHT/2)+10:
            self.color("yellow")
            self.touch="bot"
            self.bounce(self.touch,self.heading())


    
