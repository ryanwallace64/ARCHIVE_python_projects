from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.player_score = 0
        self.speed("fastest")

    def reset_score(self):
        self.player_score = 0
        self.write(f"Score: {self.player_score}", align=ALIGNMENT, font=FONT)

    def point(self):
        self.player_score += 1
        self.clear()
        self.write(f"Score: {self.player_score}", align=ALIGNMENT, font=FONT)
