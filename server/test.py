i = 1
for question in questions:
    choices = question['fake'] + [question['ans']]
    print('Question {0}: {1} \n'.format(i, question['question']))
    print('A. {0} B. {1} C. {2} D. {3}\n'.format(choices[0], choices[1], choices[2], choices[3]))
    i+=1