from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 28, "normal")


class Scoreboard(Turtle):
    """Creates a scoreboard object to keep score"""
    def __init__(self, pos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.pencolor("white")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGN, font=FONT)