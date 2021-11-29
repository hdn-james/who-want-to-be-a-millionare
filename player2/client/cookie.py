import os
import string
import random

dirname = os.path.dirname(__file__)
cookie_file = os.path.join(dirname, './cookie/cookie.txt')


def generate_random_string():
    return ''.join(random.choices(string.digits + string.ascii_letters, k=50))


def get_cookie():
    res = ""
    try:
        with open(cookie_file, 'r') as cookie:
            res = cookie.read()
    except:
        res = generate_random_string()
        with open(cookie_file, 'w') as cookie:
            cookie.write(res)
    return res
