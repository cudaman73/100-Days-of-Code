from turtle import Screen, Turtle
import random

running = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("grey47")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
winner = ""
racer = []
y_start = 180

guess = screen.textinput(title="Turtle Racing!", prompt="Who will win the race? Enter a color:")

# Turtle Initialization
for _ in range(7):
    racer.append(Turtle())
    racer[_].shape("turtle")
    racer[_].color(colors[_])
    racer[_].shapesize(1, 1, 3)
    racer[_].pu()
    racer[_].setpos(-230, y_start)
    y_start -= 60



# def move_random(_):
#     num = random.randint(0, 7)
#     racer[num].forward()
#     if racer[num].xcor() >= 250:
#         return winner = colors[num]

if guess:
    running = True

while running:
    distance = random.randint(0, 10)
    turtle = random.randint(0, 6)
    racer[turtle].forward(distance)
    if racer[turtle].xcor() >= 230:
        winner = colors[turtle]
        running = False

if guess == winner:
    print(f"You Win! the winner was {winner}.")
else:
    print(f"You lose! The winner was {winner}.")
