#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
        except OSError:  # Possibly client has left the chat.
            break

HOST = "192.168.254.10"
PORT = 33000

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()