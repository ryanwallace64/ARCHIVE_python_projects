from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 17, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increment score by 1"""
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        """Set score to 0"""
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)