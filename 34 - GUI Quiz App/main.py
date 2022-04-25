from question_model import Question
from data import *
from quiz_brain import QuizBrain
from ui import QuizInterface
import html

question_bank = []
question_data = get_data()

for question in question_data:
    question_bank.append(Question(html.unescape(question["question"]), question["correct_answer"]))


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()
