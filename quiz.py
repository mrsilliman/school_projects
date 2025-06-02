from datetime import datetime
import time

class Quiz:
    def __init__(self, file_name):
        self.alphabet_bullets = ['A', 'B', 'C', 'D']
        self.file_name = file_name
        self.questions = []
        self.potential_answers = []
        self.correct_answers = []
        self.answer_bank = {1: {'A': '', 'B': '', 'C': '', 'D': ''}, 2: {'A': '', 'B': '', 'C': '', 'D': ''},
                            3: {'A': '', 'B': '', 'C': '', 'D': ''}, 4: {'A': '', 'B': '', 'C': '', 'D': ''},
                            5: {'A': '', 'B': '', 'C': '', 'D': ''}, 6: {'A': '', 'B': '', 'C': '', 'D': ''},
                            7: {'A': '', 'B': '', 'C': '', 'D': ''}, 8: {'A': '', 'B': '', 'C': '', 'D': ''},
                            9: {'A': '', 'B': '', 'C': '', 'D': ''}, 10: {'A': '', 'B': '', 'C': '', 'D': ''}}

        self.count = 0
        self.letter = 'A'
        self.answer_result = False
        self.score = 0

    # reads questions and answers
    # nested dictionary containing question numbers and corresponding potential answer options
    def read_file(self):
        with open(self.file_name, "r") as qa:
            self.count = 1
            for line in qa:
                line = line.split(",")
                self.questions.append(line[0].strip())
                self.correct_answers.append(line[5].strip())
                for i in range(1, 5):
                    self.letter = self.alphabet_bullets[i - 1]
                    self.answer_bank[self.count][self.letter] = line[i].strip()
                self.count += 1
        return self.answer_bank

    # prints questions from nested dictionary
    def print_questions(self, question_num):
        return self.questions[(question_num - 1)]

    # prints answers from nested dictionary
    def print_answers(self, question_num):
        self.potential_answers = []
        for k in self.alphabet_bullets:
            self.potential_answers.append(self.answer_bank[question_num][k])
        return self.potential_answers

    # checks accuracy of answer
    def answer_check(self, question_num, answer):
        if answer.upper() == self.correct_answers[question_num - 1]:
            self.calculate_score()
            return 'Correct!'
        else:
            return 'Incorrect. Good try!'

    # increments score if user-provided answer is correct
    def calculate_score(self):
        self.score += 1

    # returns current score
    def display_score(self):
        return self.score

    # writes high score to text file
    def write_file(self):
        try:
            with open("Scores.txt", "a") as score_file:
                score_file.write(
                    f'{self.file_name}, {datetime.now():%Y-%m-%d, %I:%M %p}, {self.score}\n')
        except FileNotFoundError:
            with open("Scores.txt", "w") as score_file:
                score_file.write(f'{datetime.now():%Y-%m-%d, %I:%M %p}, {self.score}\n')

# inherited from Quiz
class TimedQuiz(Quiz):
    def __init__(self, file_name, timer):
        super().__init__(file_name)
        self.timer = timer
        self.start_time = 0
        self.end_time = 0

    # returns start time
    def set_timer(self):
        self.start_time = time.time()
        return self.start_time

    # returns end time
    def end_timer(self):
        self.end_time = time.time()
        return self.end_time

    # overrides parent
    # starts timer
    def print_answers(self, question_num):
        self.potential_answers = []
        for k in self.alphabet_bullets:
            self.potential_answers.append(self.answer_bank[question_num][k])
        self.set_timer()
        return self.potential_answers

    # overrides parent
    # ends timer
    # answer marked incorrect if time limit is exceeded
    def answer_check(self, question_num, answer):
        self.end_timer()
        if (self.end_time - self.start_time) <= self.timer:
            if answer.upper() == self.correct_answers[question_num - 1]:
                self.calculate_score()
                return 'Correct!'
            else:
                return 'Incorrect. Good try!'
        else:
            return 'Time\'s up. Good try!'