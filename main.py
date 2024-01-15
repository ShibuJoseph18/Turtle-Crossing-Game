from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.listen()

car_manager = CarManager()
turtle = Player()
scoreboard = Scoreboard()
screen.onkeypress(key="Up", fun=turtle.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_forward()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    if turtle.at_finish_line():
        turtle.goto_start()
        car_manager.level_up()
        scoreboard.increase_score_level()


screen.exitonclick()