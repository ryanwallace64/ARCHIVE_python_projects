from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your best", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "yellow", "purple", "green", "orange"]

rim = Turtle(shape="turtle")
bim = Turtle(shape="turtle")
yim = Turtle(shape="turtle")
pim = Turtle(shape="turtle")
gim = Turtle(shape="turtle")
oim = Turtle(shape="turtle")
names = [rim, bim, yim, pim, gim, oim]


def race_start(names):
    for _ in range(len(names)):
        location = 150
        names[_].penup()
        names[_].color(colors[_])
        names[_].goto(-230, location - (_ * 60))


def race(names):
    end_race = False
    winner = ""
    while not end_race:
        for _ in range(len(names)):
            names[_].forward(randint(1, 20))
            if names[_].xcor() >= 230:
                end_race = True
                winner = colors[_]
    print(f"The winner is the {winner} turtle!")
    if user_bet.lower() == winner:
        print("You win your bet!")
    else:
        print("You lose your bet!")


race_start(names)
race(names)



screen.exitonclick()