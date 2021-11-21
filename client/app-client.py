#!/usr/bin/env python3

import sys
import socket
import selectors
import traceback
from cookie import get_cookie
import libclient

sel = selectors.DefaultSelector()

cookie = get_cookie()

list_actions = ["get_question", "join", "answer_question"]


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
    print("starting connection to", addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = libclient.Message(sel, sock, addr, request)
    sel.register(sock, events, data=message)


if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<action> <value>")
    sys.exit(1)


host, port = '127.0.0.1', 65432
action, value = sys.argv[1], sys.argv[2]
request = create_request(action, value)
start_connection(host, port, request)

try:
    while True:
        events = sel.select(timeout=1)
        for key, mask in events:
            message = key.data
            try:
                message.process_events(mask)
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
