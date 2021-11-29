import os, sys
import subprocess

dirname = os.path.dirname(__file__)
file = os.path.join(dirname, "./appclient.py ")


def execute_action(action, value):
    if action == "join":
        print(file+f'{action} {value}')
        return subprocess.getoutput(file+f'{action} {value}')
    elif action == "get_question":
        print(file+f'{action}')
        return subprocess.getoutput(file+f'{action}')
    elif action == "answer_question":
        print(file+f'{action} {value}')
        return subprocess.getoutput(file+f'{action} "{value}"')
    elif action == "next_question":
        print(file+f'{action}')
        return subprocess.getoutput(file+f'{action}')
    elif action == "get_status":
        print(file+f'{action}')
        return subprocess.getoutput(file+f'{action}')
    elif action == "get_leaderboard":
        print(file+f'{action}')
        return subprocess.getoutput(file+f'{action}')
