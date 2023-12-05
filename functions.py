import json
from random import shuffle


def load_data(file_path) -> dict:
    """
    Loads the data from the file
    :param file_path: str
    :return: dict
    """
    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)
    return data


def shuffle_questions(questions: list) -> list:
    """
    Shuffles the questions in the list
    :param questions:
    :return:
    """
    shuffle(questions)
    return questions
