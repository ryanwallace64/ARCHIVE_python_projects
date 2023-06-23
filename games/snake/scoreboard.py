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
        with open("highscore.txt") as file:
            contents = file.read()
            self.high_score = int(contents)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increment score by 1"""
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        """Set score to 0"""
        self.score = 0
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

