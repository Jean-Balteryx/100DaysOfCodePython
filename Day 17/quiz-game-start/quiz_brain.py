class QuizBrain:

    def __init__(self, question_list):
        """Constructs a new QuizBrain object."""
        # The attribute question_number is initialized to 0
        self.question_number = 0

        # The attribute question_list is initialized with the value of the parameter question_list
        self.question_list = question_list

        # The attribute score is initialized to 0
        self.score = 0

    def next_question(self):
        """Displays the next question and asks for user answer."""
        # Retrieves question matching the attribute question_number
        question = self.question_list[self.question_number]

        # Increments the attribute question_number by 1
        self.question_number += 1

        # Asks the user for its answer and stores it
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")

        # Checks whether the user's answer is correct or not
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self):
        """Checks whether the quiz still has questions"""
        # Checks if the attribute question_number is less than the number of questions
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """Checks user's answer against the correct answer."""
        # Checks if the user's answer equals the correct answer
        if user_answer.lower() == correct_answer.lower():
            # The user got the right answer
            print("You got it right!")

            # Increments user's score by 1
            self.score += 1
        else:
            # The user got the wrong answer
            print("That's wrong.")

        # Prints the correct answer
        print(f"The correct answer was: {correct_answer}.")

        # Prints the user current score
        print(f"Your current score is: {self.score}/{self.question_number}")
