


import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
    
    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("You will be asked a series of questions. Choose the correct answer from the options provided.")
    
    def present_quiz_questions(self):
        for question in self.questions:
            print("\nQuestion:", question['question'])
            if 'options' in question:
                for i, option in enumerate(question['options'], 1):
                    print(f"{i}. {option}")
            user_answer = input("Your answer: ")
            self.evaluate_answer(question, user_answer)
    
    def evaluate_answer(self, question, user_answer):
        if user_answer.lower() == question['answer'].lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")
            print("Correct answer:", question['answer'])
    
    def display_final_results(self):
        print("\nQuiz ended.")
        print("Your score:", self.score)
        if self.score == len(self.questions):
            print("Congratulations! You got all the questions correct.")
        elif self.score >= len(self.questions) / 2:
            print("Well done! You got most of the questions correct.")
        else:
            print("Keep practicing. You can do better!")
    
    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ").lower()
        return choice == "yes"


def main():
    questions = [
        {
            'question': 'What is the capital of France?',
            'answer': 'Paris'
        },
        {
            'question': 'What is the largest mammal?',
            'answer': 'Blue whale'
        },
        {
            'question': 'What is the chemical symbol for water?',
            'answer': 'H2O'
        }
    ]

    random.shuffle(questions)  # Shuffle questions to make it more engaging
    quiz = Quiz(questions)

    while True:
        quiz.display_welcome_message()
        quiz.present_quiz_questions()
        quiz.display_final_results()

        if not quiz.play_again():
            break

if __name__ == "__main__":
    main()































