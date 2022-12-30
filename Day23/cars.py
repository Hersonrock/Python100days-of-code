from car import Car
import random
from scoreboard import SCREEN_HEIGHT,SCREEN_WIDTH
from turtle import Turtle

relative_speed=70
global_speed=SCREEN_WIDTH/relative_speed

class Cars():
    def __init__(self):
        self.traffic=[]

    def create_traffic(self):
        self.y_pos=random.randint(-SCREEN_HEIGHT/2+110,SCREEN_HEIGHT/2-110)
        car=Car(self.y_pos)
        self.traffic.append(car)

    def move(self):
        for car in self.traffic:
            car.move()
    
    def move_cars(self):
        car_moved=False
        for car in self.traffic:
            if car.speed==0:
                car.change_speed(global_speed)
                car_moved=True
            if car_moved==True:
                break

    def reset_car(self):

        for car in self.traffic:
            if car.end_check():
                self.y_pos=random.randint(-SCREEN_HEIGHT/2+110,SCREEN_HEIGHT/2-110)
                car.reset(self.y_pos)

    def traffic_init(self,init_speed):
        for car in self.traffic:
            car.change_speed(init_speed)
