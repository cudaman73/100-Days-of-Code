from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    """Creates a scoreboard on screen that reads Score: 0"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("White")
        self.goto(0, 280)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)