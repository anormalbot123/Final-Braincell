from random import shuffle
from typing import List
import os

list_questions =    [
                    {"question0": "?1", "answers": ["a","b","c"], "right": "d"},
                    {"question1": "?2", "answers": ["a","b","c"], "right": "d"},
                    {"question2": "?3", "answers": ["a","b","c"], "right": "d"},
                    {"question3": "?4", "answers": ["a","b","c"], "right": "d"},
                    {"question4": "?5", "answers": ["a","b","c"], "right": "d"},
                    {"question5": "?6", "answers": ["a","b","c"], "right": "d"}
                    ]


meme_list = os.listdir('memes')


def get_question(num_Question):
    ind = f"question{num_Question}"

    return list_questions[num_Question][ind]


def get_answers(num_Question) -> List[str]:
    answers = list_questions[num_Question]["answers"]
    answers.append(list_questions[num_Question]["right"])
    shuffle(answers)

    return answers


def get_right_ans(num_Question):
    return list_questions[num_Question]["right"]

