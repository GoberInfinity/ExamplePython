#python client.py localhost:50070,localhost:50060 127.0.0.1
#python client.py localhost:50070,localhost:50060 127.0.0.1

from __future__ import print_function
from google.protobuf import empty_pb2
from collections import deque

import sys, os
import logging, grpc
import time, threading, queue

sys.path.append(os.path.abspath(os.path.join('../..', 'gui')))
sys.path.append(os.path.abspath(os.path.join('../..', 'protos')))

import services_pb2, services_pb2_grpc
import tkinter, clientgui

class Aplication:
    def __init__(self, master):

        self.master = master
        self.queue = queue.Queue()
        self.gui =  clientgui.GuiPart(master, self.queue)
        self.counter = 0

        self.servers = deque((str(sys.argv[1])).split(','))
        self.ip = str(sys.argv[2])

        self.thread1 = threading.Thread(target=self.workerHour).start()
        self.thread2 = threading.Thread(target=self.workerBook).start()
        self.periodicCall()

    def periodicCall(self):
        self.gui.processIncoming()
        self.master.after(100, self.periodicCall)

    def workerHour(self):
        server1 = self.servers[0].split(':')
        ip_server = server1[0]
        port_server = server1[1]
        print(server1)
        while True:
            try:
                with grpc.insecure_channel(ip_server+':'+port_server) as channel:
                    stub = services_pb2_grpc.InformationStub(channel)
                    response = stub.SendHour(empty_pb2.Empty())
                    self.queue.put("T_" + response.hour)
            except:
                self.servers.append(self.servers.popleft())
                server1 = self.servers[0].split(':')
                ip_server = server1[0]
                port_server = server1[1]
                print("Error trying to get the clock trying new server")
            time.sleep(1)

    def workerBook(self):
        server1 = self.servers[0].split(':')
        ip_server = server1[0]
        port_server = server1[1]
        while True:
            if self.gui.getIsRequest():
                    self.gui.turnOffIsRequest()
                    try:
                        with grpc.insecure_channel(ip_server+':'+port_server) as channel:
                            stub = services_pb2_grpc.InformationStub(channel)
                            metadata = [('ip', self.ip)]
                            response2 = stub.SendBook(empty_pb2.Empty() , metadata = metadata)
                            self.queue.put("B_" + response2.book)
                    except:
                        self.servers.append(self.servers.popleft())
                        server1 = self.servers[0].split(':')
                        ip_server = server1[0]
                        port_server = server1[1]
                        print("Error trying to get a book trying new server")
        time.sleep(1)

root = tkinter.Tk()
client = Aplication(root)
root.mainloop()
