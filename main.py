from config import QUESTIONS_PATH
from class_question import Question
from functions import load_data, shuffle_questions

questions_data = load_data(QUESTIONS_PATH)

questions = []
for question in questions_data:
    questions.append(
        Question(
            question=question["q"],
            difficulty=question["d"],
            answer=question["a"],
        )
    )

shuffle_questions = shuffle_questions(questions)

if __name__ == "__main__":
    print("Hello! Welcome to the quiz. You will be asked 5 questions. Good luck!")
    for question in shuffle_questions:
        print(question.show_question())
        user_answer = input("Your answer: ")
        question.user_answer = user_answer

        if question.is_correct():
            print(question.get_feedback())
            print(f"Your points: {question.get_points()}")
        else:
            print(question.get_feedback())

    print(
        f"Thanks for playing!\n Right answers: {sum([1 for question in shuffle_questions if question.is_correct()])}.\n"
        f"Your total points: {sum([question.get_points() for question in shuffle_questions])}")
