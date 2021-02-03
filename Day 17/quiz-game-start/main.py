# Imports Question and QuizBrain classes
from question_model import Question
from quiz_brain import QuizBrain

# Imports quiz data
from data import question_data

# Creates an empty list that will contain Question objects
question_bank = []

# Goes through all questions and creates matching Question objects
for question in question_data:
    # Creates a Question object using the text and correct answer of the current question from quiz data
    question = Question(question["question"], question["correct_answer"])

    # Adds the new Question object to the question bank
    question_bank.append(question)

# Creates a QuizBrain object using the question bank
quiz = QuizBrain(question_bank)

# Goes through all quiz questions
while quiz.still_has_questions():
    # Displays the next question and process user's answer
    quiz.next_question()

# Prints end game message
print("You've completed the quiz!")

# Prints user's final score
print(f"Your final score is {quiz.score}/{quiz.question_number}.")
