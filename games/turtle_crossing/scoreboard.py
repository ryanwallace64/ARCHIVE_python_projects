from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-270, 250)
        self.level = 0

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)

    def reset_level(self):
        self.level = 0

    def game_over(self):
        self.goto(0, 100)
        self.write("GAME OVER", align="center", font=FONT)
