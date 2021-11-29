#!/usr/bin/env python3

import sys
import socket
import selectors
import traceback
from cookie import get_cookie
from libclient import *


sel = selectors.DefaultSelector()

mycookie = get_cookie()

list_actions = ["get_question", "join",
                "answer_question", "next_question", "get_status", "get_leaderboard"]
host, port = '127.0.0.1', 65432

def create_request(action, value):
    if action in list_actions:
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=value),
        )
    else:
        return dict(
            type="binary/custom-client-binary-type",
            encoding="binary",
            content=bytes(action + value, encoding="utf-8"),
        )


def start_connection(host, port, request):
    addr = (host, port)
    # print("starting connection to", addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = Message(sel, sock, addr, request)
    sel.register(sock, events, data=message)


def run():
    result_response = None
    try:
        while True:
            events = sel.select(timeout=1)
            for key, mask in events:
                message = key.data
                try:
                    result = message.process_events(mask)
                    if result:
                        result_response = result
                        # print(result_response)
                except Exception:
                    print(
                        "main: error: exception for",
                        f"{message.addr}:\n{traceback.format_exc()}",
                    )
                    message.close()
            if not sel.get_map():
                break
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        sel.close()
        return result_response


def communication(action, value):
    request = create_request(action, value)
    start_connection(host, port, request)
    return run()

def join(username):
    value_str = f'{{"cookie":"{mycookie}","username":"{username}"}}'
    return communication(action="join",value=value_str)

def get_question():
    value_str = f'{{"cookie":"{mycookie}"}}'
    return communication(action="get_question",value=value_str)

def answer_question(answer):
    value_str = f'{{"cookie":"{mycookie}","answer":"{answer}"}}'
    return communication(action="answer_question",value=value_str)

def next_question():
    value_str = f'{{"cookie":"{mycookie}"}}'
    return communication(action="next_question",value=value_str)

def get_status():
    value_str = f'{{"cookie":"{mycookie}"}}'
    return communication(action="get_status",value=value_str)

def get_leaderboard():
    value_str = f'{{"cookie":"{mycookie}"}}'
    return communication(action="get_leaderboard",value=value_str)

action = sys.argv[1]

if action == "join":
    print(join(sys.argv[2]))
elif action == "get_question":
    print(get_question())
elif action == "answer_question":
    print(answer_question(sys.argv[2]))
elif action == "next_question":
    print(next_question())
elif action == "get_status":
    print(get_status())
elif action == "get_leaderboard":
    print(get_leaderboard())