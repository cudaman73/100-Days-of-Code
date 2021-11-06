from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    """Creates 3-segment snake and defines movement"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in START_POS:
            self.add_segment(_)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
