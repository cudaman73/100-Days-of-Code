from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

running = True
while running:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
