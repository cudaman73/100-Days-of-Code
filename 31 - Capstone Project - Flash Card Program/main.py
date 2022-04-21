from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
index = 0
try:
    word_dict = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_dict = pandas.read_csv("data/french_words.csv")

# program should randomly pick a word from the csv file, display the french version of the word,
# then change to the english version after 3 seconds, then wait for user input. if the user clicks
# correct, then it will remove that word from the list of words, since we know it already. if the
# user clicks no, then the program will start over, pick another word at random.

# possible alternatives - I imported and used the dataframe natively, which is fine, but definitely
# overkill for this project. It likely would've been better to use panda's .to_dict(orient="records")
# to convert the dataframe to a standard python dictionary, it would make it slightly easier to parse
# the code i've written, but it's really a minor difference.


def flip_card(english_word):
    flash_card.itemconfig(language_text, text="English", fill="white")
    flash_card.itemconfig(word, text=english_word, fill="white")
    flash_card.itemconfig(card, image=card_back)


def get_word():
    global index
    index = random.randint(0, len(word_dict))
    french_word = word_dict["French"][index]
    english_word = word_dict["English"][index]
    flash_card.itemconfig(card, image=card_front)
    flash_card.itemconfig(language_text, text="French", fill="black")
    flash_card.itemconfig(word, text=french_word, fill="black")
    flash_card.flip = flash_card.after(3000, flip_card, english_word)


# Right and wrong programs
def wrong():
    if flash_card.flip:
        flash_card.after_cancel(flash_card.flip)
        flash_card.flip = None
    get_word()


def right():
    global index
    if flash_card.flip:
        flash_card.after_cancel(flash_card.flip)
        flash_card.flip = None
    word_dict.drop([index])
    word_dict.to_csv("data/words_to_learn.csv")
    get_word()


# UI Setup
window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
no_image = PhotoImage(file="images/wrong.png")
yes_image = PhotoImage(file="images/right.png")

flash_card = Canvas(height=526, width=800)
flash_card.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card = flash_card.create_image(400, 263, image=card_front)
language_text = flash_card.create_text(400, 150, font=("Ariel", 40, "italic"), text="")
word = flash_card.create_text(400, 263, font=("Ariel", 60, "bold"), text="")

no_button = Button(image=no_image, command=wrong, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
yes_button = Button(image=yes_image, command=right, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)

flash_card.grid(column=0, row=0, columnspan=2)
no_button.grid(column=0, row=1)
yes_button.grid(column=1, row=1)

get_word()
window.mainloop()
