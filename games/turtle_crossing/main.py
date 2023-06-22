import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
screen.setup(width=600, height=600)


def reset_screen():
    global player
    screen.clearscreen()
    screen.tracer(0)
    player = Player()
    screen.listen()
    screen.onkey(player.move, key="Up")


reset_screen()

scoreboard = Scoreboard()
scoreboard.update_level()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        reset_screen()
        car_manager.cars = []
        scoreboard.update_level()
        car_manager.increase_speed()
        car_manager.spawn_frequency -= 10

    for car in range(len(car_manager.cars)):
        if car_manager.cars[car].distance(player) < 20 or -20 < car_manager.cars[car].ycor() - player.ycor() < 20 and \
                -20 < car_manager.cars[car].xcor() < 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
