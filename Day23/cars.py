from car import Car
import random
from scoreboard import SCREEN_HEIGHT,SCREEN_WIDTH
from turtle import Turtle

class Cars():
    def __init__(self):
        self.traffic=[]

    def create_traffic(self,number):
        for i in range(number+1):
            self.y_pos=random.randint(-SCREEN_HEIGHT/2+110,SCREEN_HEIGHT/2-110)
            car=Car(self.y_pos)
            self.traffic.append(car)

    def move(self,speed):
        for car in self.traffic:
            car.forward(speed)

    def move_init(self):
        for car in self.traffic:
            ran_speed=random.randint(0,SCREEN_WIDTH)
            car.move(ran_speed)

    def reset_car(self):
        for car in self.traffic:
            if car.end_check():
                self.y_pos=random.randint(-SCREEN_HEIGHT/2+110,SCREEN_HEIGHT/2-110)
                car.reset(self.y_pos)
