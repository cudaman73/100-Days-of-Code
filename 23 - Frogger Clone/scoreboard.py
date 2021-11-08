from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Creates a scoreboard object to track the player's level"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
