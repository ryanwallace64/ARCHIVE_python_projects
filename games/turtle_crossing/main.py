import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
scoreboard.update_level()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        scoreboard.update_level()
        car_manager.increase_speed()
        car_manager.spawn_frequency -= 7
        player.reset_position()

    for car in range(len(car_manager.cars)):
        if car_manager.cars[car].distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
