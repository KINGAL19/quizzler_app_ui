from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []  # 裝著question_model物件

for question in question_data:  # 把清單中的字典一個一個拿出來
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)  # 重新裝成question_model物件
    question_bank.append(new_question)  # 再裝進question_bank清單


quiz = QuizBrain(question_bank)  # 把question_model物件處理過的QuizBrain物件
quiz_ui = QuizInterface(quiz)  # 把(question_model-> QuizBrain)QuizBrain物件處理過的QuizInterface物件


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
