from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        if self.x_move > 5:
            self.x_move *= -1.07
        else:
            self.x_move *= -1.15

    def reset(self):
        self.bounce_x()
        self.x_move = 3
        self.y_move = 3
        self.goto(0, 0)
