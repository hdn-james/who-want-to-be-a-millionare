import selectors
import types
import socket
import json
import random

def load_question(path):
    f = open(path, "r")
    questions = json.load(f)
    f.close()
    return questions

def accept_connection(socket):
    connection, address = socket.accept()
    print('Accepted connection from', address)
    connection.setblocking(False)
    data = types.SimpleNamespace(addr=address, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(connection, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print("Closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing',repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb) # reading to write
            data.outb = data.outb[sent:]
            
questions = load_question("./server/lib/questions.json")

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
sel = selectors.DefaultSelector()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print("Listening on", (HOST, PORT))
lsock.setblocking(False)

sel.register(lsock, selectors.EVENT_READ, data=None)

while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_connection(key.fileobj)
        else:
            service_connection(key, mask)
