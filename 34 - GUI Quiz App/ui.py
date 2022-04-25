from tkinter import *
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz, color=THEME_COLOR):
        self.quiz = quiz
        self.question = str
        self.answer = str
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=color)
        self.score = Label(text="Score: 0", bg=color, fg="white")
        self.score.grid(row=0, column=1)
        self.question_window = Canvas(self.window, height=300, width=350)
        self.question_window.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.question_window.create_text(175, 150, font=("Arial", 20, "italic"), text="", width=300)
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(self.window, command=lambda: self.make_guess("true"), image=self.true_image, bg=color,
                                  highlightthickness=0, borderwidth=0)
        self.true_button.grid(row=2, column=0)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(self.window, command=lambda: self.make_guess("false"), image=self.false_image, bg=color,
                                   highlightthickness=0, borderwidth=0)
        self.false_button.grid(row=2, column=1)
        self.ask_question()
        self.window.mainloop()

    def ask_question(self):
        self.question_window.config(bg="white")
        self.question, self.answer = self.quiz.next_question()
        self.question_window.itemconfig(self.question_text, text=f"{self.question}")

    def make_guess(self, response):
        guess, score = self.quiz.check_answer(response, self.answer)
        self.score.config(text=f"Score: {score}")
        if guess:
            self.question_window.config(bg="green")
        else:
            self.question_window.config(bg="red")
        if self.quiz.still_has_questions():
            self.window.after(2000, self.ask_question)
        else:
            print("You've completed the quiz")
            print(f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            exit(0)
