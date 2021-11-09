from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Blue")
        self.shape("circle")
        self.shapesize(0.5, 0.5, 1)
        self.speed("fastest")
        self.pu()
        self.is_eaten()

    def is_eaten(self):
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        self.setpos(pos_x, pos_y)

    def reset_self(self):
        self.is_eaten()
