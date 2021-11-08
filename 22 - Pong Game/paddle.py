from turtle import Turtle
START_POSITION = [(-350, 0), (350, 0)]


class Paddle (Turtle):

    """Creates a paddle for the user to control in the game"""
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 5, 1)
        self.setheading(90)
        if side == "left":
            self.goto(START_POSITION[0])
        elif side == "right":
            self.goto(START_POSITION[1])

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)