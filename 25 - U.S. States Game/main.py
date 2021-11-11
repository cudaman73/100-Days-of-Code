from turtle import Screen
from state import State, key
import pandas

named_states = []
missed_states = {"state": [], "location": []}

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.title("Name the States!")
screen.listen()
guess = ""

# Alternative way to handle answer guessing logic (from the video):
list_of_states = key.state.to_list()

while len(named_states) < 50:
    if len(named_states) == 0:
        guess = screen.textinput(f"{len(named_states)}/50 States Correct", "What's a state's name?").title()

    if guess == "Exit":
        break

    if guess in list_of_states:
        named_states.append(guess)
        state = State(guess)

    guess = screen.textinput(f"{len(named_states)}/50 States Correct", "What's another state's name?").title()

# once game is over - let the user know which states they missed in a csv
for state in list_of_states:
    if state not in named_states:
        data = key[key.state == state]
        missed_states["state"].append(state)
        missed_states["location"].append((int(data.x), int(data.y)))

pandas.DataFrame(missed_states).to_csv("missed_states.csv")
