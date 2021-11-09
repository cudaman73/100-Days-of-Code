from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    """Creates a scoreboard on screen that reads Score: 0"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.read_high_score())
        self.penup()
        self.hideturtle()
        self.pencolor("White")
        self.goto(0, 280)
        self.update_score()

    def update_high_score(self):
        f = open("score.txt", "w")
        f.write(f"{self.high_score}")
        f.close()

    def read_high_score(self):
        f = open("score.txt")
        score = f.read()
        f.close()
        return score

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_self(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write("Game over, press N key to start over!", move=False, align=ALIGNMENT, font=FONT)
    #     self.reset_self()
