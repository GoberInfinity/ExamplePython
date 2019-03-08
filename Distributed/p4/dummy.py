#!/usr/bin/env python3

import socket
import time
import sys

HOST = 'localhost'  # The server's hostname or IP address
PORT = 50010        # The port used by the server


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    s.send(b'Hello, world')
    data = s.recv(1024)
    print(data)
    sys.stdout.flush()
    time.sleep(1)

s.close()
