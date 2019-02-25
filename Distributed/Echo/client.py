#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 11:17:27 2019

@author: Gober
"""


import sys
import time 
from socket import *              # portable socket interface plus constants
serverHost = 'localhost'          # server name, or: 'starship.python.net'
serverPort = 50007                # non-reserved port used by the server

message = [b'Hello network world']          # default text to send to server
                                            # requires bytes: b'' or str,encode()
if len(sys.argv) > 1:       
    serverHost = sys.argv[1]                # server from cmd line arg 1
    if len(sys.argv) > 2:                   # text from cmd line args 2..n
        message = (x.encode() for x in sys.argv[2:])  

sockobj = socket(AF_INET, SOCK_STREAM)      # make a TCP/IP socket object
sockobj.connect((serverHost, serverPort))   # connect to server machine + port

while True:
    sockobj.send(message[0])                      # send line to server over socket
    data = sockobj.recv(1024)               # receive line from server: up to 1k
    print('Client received:', data)         # bytes are quoted, was `x`, repr(x)
    sys.stdout.flush()
    time.sleep(1)
	

sockobj.close() 