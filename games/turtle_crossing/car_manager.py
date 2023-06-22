from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class CarManager:
    def __init__(self):
        self.cars = []
        self.spawn_frequency = 80
        self.move_distance = STARTING_MOVE_DISTANCE

    def new_car(self):
        if random.randint(1, 100) >= self.spawn_frequency:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.goto(290, random.randint(-290, 290))
            new_car.setheading(180)
            self.cars.append(new_car)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

    def move_cars(self):
        for car in range(len(self.cars)):
            self.cars[car].forward(self.move_distance)
