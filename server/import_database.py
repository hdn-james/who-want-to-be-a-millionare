import json
import os

dirname = os.path.dirname(__file__)
questions_file = os.path.join(dirname, './lib/questions.json')
correct_answer = os.path.join(dirname, "./lib/correct_answer.json")


def read_questions():
    with open(questions_file, 'r') as questions:
        ques_data = json.load(questions)
    return ques_data


def read_correct_answer():
    with open(correct_answer, 'r') as cr_ans:
        cr_ans_data = json.load(cr_ans)
    return cr_ans_data
