class QuizBrain:

    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0


    def next_question(self):
        """Prints current question, returns response from user"""
        q_current = self.q_list[self.q_number]
        self.q_number += 1
        response = input(f"Q.{self.q_number}: {q_current.text} (True/False):")
        self.check_answer(response, q_current.answer)

    def still_has_questions(self):
        return self.q_number < len(self.q_list)


    def check_answer(self, response, answer):
        """returns Correct or Incorrect based on the response matching the answer"""
        if response.lower() == answer.lower():
            print("Correct! Moving on...")
            self.score += 1
        else:
            print("Incorrect. Next Question...")
        print(f"The correct answer was {answer}.")
        print(f"Your current score is: {self.score}/{self.q_number}.")