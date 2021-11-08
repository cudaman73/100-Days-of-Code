from turtle import Turtle
import random

class Ball(Turtle):

    """Creates a ball object that will move automatically"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed = 1
        self.x_move = 10
        self.y_move = 10

    def increase_speed(self):
        self.x_move *= 1.05
        self.y_move *= 1.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1
        self.increase_speed()

    def x_bounce(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_ball(self, xcor):
        if xcor > 0:
            self.x_move = -10
        if xcor < 0:
            self.x_move = 10
        self.goto(0, 0)
        self.y_move = random.choice([-10, 10])
