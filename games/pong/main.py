from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard
import time

STARTING_POSITIONS = [(-385, 0), (377, 0)]
WALL_POSITIONS = [(0, 301), (0, -293)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

top_wall = Wall(WALL_POSITIONS[0])
bottom_wall = Wall(WALL_POSITIONS[1])
l_paddle = Paddle(STARTING_POSITIONS[0])
r_paddle = Paddle(STARTING_POSITIONS[1])
ball = Ball()

l_scoreboard = Scoreboard((-100, 270))
r_scoreboard = Scoreboard((100, 270))
l_scoreboard.reset_score()
r_scoreboard.reset_score()

screen.onkey(r_paddle.move_up, key="Up")
screen.onkey(r_paddle.move_down, key="Down")
screen.onkey(l_paddle.move_up, key="w")
screen.onkey(l_paddle.move_down, key="s")

game_on = True
while game_on:
    time.sleep(.02)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -275:
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -360 or ball.distance(r_paddle) < 50 and ball.xcor() > 360 or \
            ball.distance(l_paddle) < 20 or ball.distance(r_paddle) < 20:
        ball.bounce_x()

    if ball.xcor() > 400:
        l_scoreboard.point()
        time.sleep(1.5)
        ball.reset()

    if ball.xcor() < -405:
        r_scoreboard.point()
        time.sleep(1.5)
        ball.reset()

screen.exitonclick()
