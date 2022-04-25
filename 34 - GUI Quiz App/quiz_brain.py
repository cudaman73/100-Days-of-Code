class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self) -> int:
        return self.question_number < len(self.question_list)

    def next_question(self) -> tuple[str, str]:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        return current_question.text, current_question.answer

    def check_answer(self, response, answer) -> tuple[bool, int]:
        if response.lower() == answer.lower():
            self.score += 1
            return True, self.score
        else:
            return False, self.score
