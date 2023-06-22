from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.goto(position)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.back(20)