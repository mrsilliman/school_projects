import tkinter as tk
from tkinter import ttk
from quiz import Quiz, TimedQuiz

class TriviaGameFrame:
    def __init__(self, master):
        self.master = master

        self.test_message1 = ""
        self.test_message2 = ""
        self.test_message3 = ""
        self.test_message3 = ""
        self.test_message4 = ""
        self.potential_answers = []
        self.button_num = ""
        self.quiz = Quiz("Office_Trivia.txt")
        self.timedquiz = TimedQuiz("Office_Trivia.txt", 10)
        self.question_count = 0
        self.new_entries = []
        self.option_num = 0

        self.question = tk.StringVar()
        self.answer1 = tk.StringVar()
        self.answer2 = tk.StringVar()
        self.answer3 = tk.StringVar()
        self.answer4 = tk.StringVar()
        self.correct_answer = tk.StringVar()

    #clears frame of all widget
    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def display_label(self, message1):
        self.test_message1 = message1
        ttk.Label(self.master, text=self.test_message1).grid(
            column=0, row=0, sticky=tk.W)

    def answer_label(self, message1):
        self.test_message1 = message1
        ttk.Label(self.master, text=self.test_message1).grid(
            column=0, row=7, sticky=tk.W)

    # options include regular and timed quiz
    def option_trigger(self, option_num):
        if option_num is not None:
            self.option_num = option_num
            if option_num == 1:
                self.quiz.read_file()
                self.get_quiz(1)
            else:
                self.timedquiz.read_file()
                self.get_timedquiz(1)
        return self.option_num

    def score_label(self):
        if self.option_num == 1:
            ttk.Label(self.master, text="Current score: " + str(self.quiz.display_score())).grid(
            column=8, row=4, sticky=tk.W)
        else:
            ttk.Label(self.master, text="Current score: " + str(self.timedquiz.display_score())).grid(
                column=8, row=4, sticky=tk.W)

    # allows for user input of questions and answers when file is not found
    def qa_entries(self, num):
        self.clear_frame()
        self.display_label("File not found. Questions and potential answers must be entered.")

        ttk.Label(self.master, text="Question " + str(num)).grid(
            column=0, row=1, sticky=tk.W)
        ttk.Entry(self.master, width=25, textvariable=self.question).grid(column=1, row=1, padx=3)

        ttk.Label(self.master, text="Answer 1").grid(
            column=0, row=2, sticky=tk.W)
        ttk.Entry(self.master, width=25, textvariable=self.answer1).grid(column=1, row=2, padx=3)

        ttk.Label(self.master, text="Answer 2").grid(
            column=0, row=3, sticky=tk.W)
        ttk.Entry(self.master, width=25, textvariable=self.answer2).grid(column=1, row=3, padx=3)

        ttk.Label(self.master, text="Answer 3").grid(
            column=0, row=4, sticky=tk.W)
        ttk.Entry(self.master, width=25, textvariable=self.answer3).grid(column=1, row=4, padx=3)

        ttk.Label(self.master, text="Answer 4").grid(
            column=0, row=5, sticky=tk.W)
        ttk.Entry(self.master, width=25, textvariable=self.answer4).grid(column=1, row=5, padx=3)

        ttk.Label(self.master, text="Correct answer [A, B, C, D]").grid(
            column=0, row=6, sticky=tk.W)
        ttk.Entry(self.master, width=25, textvariable=self.correct_answer).grid(column=1, row=6, padx=3)

        ttk.Button(self.master, text="Submit", command=lambda: self.initialize_answers(num)).grid(
            column=1, row=7, padx=3)

    # appends user-inputted questions and answers to file
    def initialize_answers(self, num):
        if self.correct_answer.get().upper() not in ['A', 'B', 'C', 'D']:
            self.qa_entries(num)
        else:
            self.new_entries = [self.question.get(), self.answer1.get(), self.answer2.get(),
                                self.answer3.get(), self.answer4.get(), self.correct_answer.get().upper()]

            with open("Office_Trivia.txt", "a") as new_qa:
                new_qa.write(f'{self.new_entries[0]}, {self.new_entries[1]}, {self.new_entries[2]}, {self.new_entries[3]}, '
                                 f'{self.new_entries[4]}, {self.new_entries[5]}\n')

            self.new_entries = []
            self.question.set("")
            self.answer1.set("")
            self.answer2.set("")
            self.answer3.set("")
            self.answer4.set("")
            self.correct_answer.set("")

            if num < 10:
                self.qa_entries(num + 1)
            else:
                self.game_setup()

    def button_trigger(self, button_num):
        if button_num is not None:
            if self.option_num == 1:
                self.answer_label(self.quiz.answer_check(self.question_count, chr(button_num + 64)))
            else:
                self.answer_label(self.timedquiz.answer_check(self.question_count, chr(button_num + 64)))

    # trigger for next question button
    def question_trigger(self):
        try:
            if self.option_num == 1:
                self.get_quiz(self.question_count + 1)
            else:
                self.get_timedquiz(self.question_count + 1)
        except Exception as e:
            if self.option_num == 1:
                self.quiz.write_file()
            else:
                self.timedquiz.write_file()
            self.clear_frame()
            self.display_label("Good game!")

    # for regular vs timed trivia options
    def two_buttons(self, message1, message2):
        self.test_message1 = message1
        self.test_message2 = message2

        ttk.Button(self.master, text=self.test_message1, command=lambda: self.option_trigger(1)).grid(
        column=0, row=1, padx=3, sticky='w')
        ttk.Button(self.master, text=self.test_message2, command=lambda: self.option_trigger(2)).grid(
            column=0, row=2, padx=3, sticky='w')

    # for trivia question selection
    def four_buttons(self, answers):
        self.potential_answers = answers
        for k in range(1, 5):
            ttk.Button(self.master, text=self.potential_answers[k-1], command=lambda k=k: self.button_trigger(k)).grid(
            column=0, row=k+1, padx=3, sticky='w')

    def next_question(self):
        ttk.Button(self.master, text="Next question", command=self.question_trigger).grid(
                column=8, row=2, padx=3)

    # writes initial file if file not found
    def file_handing(self):
        try:
            self.quiz.read_file()
            self.game_setup()
        except FileNotFoundError:
            with open("Office_Trivia.txt", "w") as file:
                pass
            self.qa_entries(1)

    # determines the type of game
    def game_setup(self):
        self.clear_frame()
        self.display_label("Welcome to Office Trivia!")
        self.two_buttons("Regular Trivia", "Timed Trivia (10 sec)")

    # for regular quiz trivia
    def get_quiz(self, question_count):
        self.question_count = question_count
        self.clear_frame()
        self.next_question()
        self.score_label()
        self.display_label(self.quiz.print_questions(question_count))
        self.four_buttons(self.quiz.print_answers(question_count))

    # for timed quiz trivia
    def get_timedquiz(self, question_count):
        self.question_count = question_count
        self.clear_frame()
        self.next_question()
        self.score_label()
        self.display_label(self.timedquiz.print_questions(question_count))
        self.four_buttons(self.timedquiz.print_answers(question_count))