from turtle import Turtle
import pandas

key = pandas.read_csv("50_states.csv")


class State(Turtle):
    """creates an object to write the states name after identifying it correctly, and
    moves to the correct spot on the map"""
    def __init__(self, name):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.new_x = 0
        self.new_y = 0
        self.move(name)
        self.write(name)

    def move(self, name):
        data = key[key.state == name]
        self.new_x = int(data.x)
        self.new_y = int(data.y)
        self.goto(self.new_x, self.new_y)
