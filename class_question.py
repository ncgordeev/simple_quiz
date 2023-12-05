class Question:

    def __init__(self, question: str, difficulty: int, answer: str) -> None:
        self.question = question
        self.difficulty = int(difficulty)
        self.answer = answer

        self.is_asked = False
        self.user_answer = None
        self.points = self.difficulty * 10

    def __str__(self) -> str:
        return f"{self.question}\nDifficulty: {self.difficulty}\nAnswer: {self.answer}"

    def __repr__(self) -> str:
        return (f"Question: {self.question}\nDifficulty: {self.difficulty}\nAnswer: {self.answer}\n"
                f"Is asked: {self.is_asked}\nUser answer: {self.user_answer}\nPoints: {self.points}")

    def get_points(self) -> int:
        """
        Returns the points of the question
        :return: int
        """
        return self.points

    def is_correct(self) -> bool:
        """
        Checks if the user answer is correct
        :return: bool
        """
        if self.user_answer == self.answer:
            return True
        else:
            return False

    def show_question(self) -> str:
        """
        Shows the question
        :return: str
        """
        return f"Question: {self.question}\nDifficulty: {self.difficulty}"

    def get_feedback(self) -> str:
        """
        Returns the feedback of the question
        :return: str
        """
        if self.is_correct():
            return f"Correct! You earned {self.points} points!"
        else:
            return f"Wrong! Correct answer is {self.answer}"
