import json

def load_question(path):
    f = open(path, "r")
    questions = json.load(f)
    f.close()
    return questions
    
    
questions = load_question("questions.json")
for question in questions:
    print('{0} \n'.format(question))