#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from socket import *
serverHost = 'localhost'
serverPort = 50007

message = [b'Hello network world']
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

while True:
    sockobj.send(message[0])
    data = sockobj.recv(1024)
    print('Client received:', data)
    sys.stdout.flush()
    time.sleep(1)

sockobj.close()
