from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.score = 0

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas_text = self.canvas.create_text(
            150, 125,
            width=280,
            text='',
            fill=THEME_COLOR,
            font=("Ariel", 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # Label
        self.score_label = Label(text=f'Score: {self.score}', bg=THEME_COLOR, fg='white', font=("Ariel", 12, 'italic'))
        self.score_label.grid(row=0, column=1)
        # Button
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=00, padx=20, pady=20, command=self.true_clicked)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, padx=20, pady=20, command=self.false_clicked)
        self.false_button.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f'Score: {self.quiz_brain.score}')
        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(self.canvas_text, text=self.quiz_brain.next_question())
        else:
            self.canvas.itemconfig(self.canvas_text,
                                   width=280,
                                   text=f'Game Finished! You got '
                                        f'\n{self.quiz_brain.score}/{self.quiz_brain.question_number}',
                                   font=("Ariel", 16, 'italic'))
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def feed_back(self, is_right):
        self.window.after(1000, self.next_question)
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

    def true_clicked(self):
        is_right = self.quiz_brain.check_answer('True')
        self.feed_back(is_right)

    def false_clicked(self):
        is_right = self.quiz_brain.check_answer('False')
        self.feed_back(is_right)
