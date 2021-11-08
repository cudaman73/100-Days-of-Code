import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Scoreboard()
cars = CarManager()
player = Player()
car_chance = 0.833
screen.listen()
screen.onkeypress(player.move, "Up")


def reset_player():
    player.goto(0, -280)
    score.increase_level()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.random() > car_chance:
        cars.create_car()
    cars.move_cars()

    for car in cars.car_array:
        if player.distance(car) < 15:
            score.game_over()
            game_is_on = False

    if player.ycor() > 280:
        reset_player()
        cars.speed_up()
        car_chance *= 0.9

screen.exitonclick()
