from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()
score_left = Scoreboard((-20, 250))
score_right = Scoreboard((20, 250))

screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")


def reset_screen(xcor):
    if xcor > 380:
        score_right.increase_score()
    if xcor < -380:
        score_left.increase_score()
    ball.reset_ball(ball.xcor())
    left_paddle.goto(-350, 0)
    right_paddle.goto(350, 0)
    screen.update()
    time.sleep(2)


game_running = True
while game_running:
    time.sleep(.06)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_bounce()

    if ball.distance(right_paddle) < 60 and ball.xcor() > 340 or ball.distance(left_paddle) < 60 and ball.xcor() < -340:
        ball.x_bounce()

    if ball.xcor() > 380 or ball.xcor() < -380:
        reset_screen(ball.xcor())


screen.exitonclick()
