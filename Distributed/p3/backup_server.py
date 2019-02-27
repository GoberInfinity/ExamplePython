#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import os
from socket import *
serverHost = 'localhost'
serverPort = 50007

CHUNK_SIZE = 8 * 1024

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

while True:

    #sockobj.send(b"1")
    total = sockobj.recv(1024)
    try:
        total_size = int(total.decode())
    except ValueError:
        total_size = 0
        continue
    terminated = False
    sockobj.send(b"Ready to recieve")
    print(total_size)
    with open('dump_backup.sql','wb') as f:
        print("File opened")
        size = 0
        while True:
            print("Recieveing Data")
            data2 = sockobj.recv(1024)
            if not data2: break
            size += len(data2)
            f.write(data2)
            print(size)
            if size == int(total_size):
                terminated = True
                break
    if terminated:
        os.system('rm -rf dump_database.db')
        os.system('cat dump_backup.sql | sqlite3 dump_database.db')
        print("CREATED")
        terminated = False

    print('Up to date')
    sys.stdout.flush()
    time.sleep(0.5)

sockobj.close()
