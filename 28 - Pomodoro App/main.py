# Pomodoro technique - assign task -> 25 min work -> 5 min break -> repeat 4x -> 15-30 min break
# once you click start - label changes to work, timer counts down from 25 minutes
# when it switches to break - app bounces to top-most window, 5 minute timer, check mark appears to
# let you know how many pomodoros you've completed
# has reset button
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_id = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_id)
    count_label.config(text="")
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_loop():
    global reps
    reps += 1

    if reps == 8:
        title_label.config(text="Rest", fg=RED)
        canvas.itemconfig(timer, text="20:00")
        count_down(10)
    elif reps % 2 == 0:
        window.focus()
        title_label.config(text="Break", fg=PINK)
        canvas.itemconfig(timer, text="5:00")
        count_down(3)
    else:
        title_label.config(text="Work", fg=GREEN)
        canvas.itemconfig(timer, text="25:00")
        count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(seconds):
    global reps
    min_remain = seconds // 60
    if min_remain < 10:
        min_remain = f'0{min_remain}'
    sec_remain = seconds % 60
    if sec_remain < 10:
        sec_remain = f'0{sec_remain}'
    canvas.itemconfig(timer, text=f"{min_remain}:{sec_remain}")
    if seconds > 0:
        global timer_id
        timer_id = window.after(1000, count_down, seconds - 1)
    else:
        timer_loop()
        # add a checkmark each time we complete a work session
        count_label.config(text=u"\u2713" * (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

background = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=background)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

title_label = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
title_label.config(padx=5, pady=5)

count_label = Label(font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
count_label.config(padx=5, pady=5)

start_button = Button(text="Start", command=timer_loop, highlightthickness=0)
start_button.config(padx=5, pady=5)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.config(padx=5, pady=5)

title_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
count_label.grid(column=1, row=3)

window.mainloop()
