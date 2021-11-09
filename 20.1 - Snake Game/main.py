from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def restart_game():
    snake.reset_self()
    scoreboard.reset_self()
    food.reset_self()


running = True
while running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect food collision
    if snake.head.distance(food) < 15:
        snake.extend()
        food.is_eaten()
        scoreboard.increase_score()

    # detect wall collision
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.reset_self()
        snake.reset_self()

    # detect self collision, slicing out head from list
    for _ in snake.segments[1:]:
        if snake.head.distance(_) < 10:
            scoreboard.reset_self()
            snake.reset_self()


screen.exitonclick()
