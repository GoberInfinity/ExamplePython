from __future__ import print_function
from google.protobuf import empty_pb2

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

        self.thread1 = threading.Thread(target=self.workerThreadNewtork).start()
        self.periodicCall()

    def periodicCall(self):
        self.gui.processIncoming()
        self.master.after(100, self.periodicCall)

    def workerThreadNewtork(self):
        while True:
            """
            is_editable = self.gui.getIsRequest()
            message = [str(is_editable).encode()]
            if is_editable:
                self.gui.turnOffIsRequest()
            self.sockobj.send(message[0])
            data = self.sockobj.recv(1024)
            self.queue.put(data)
            self.counter +=1
            time.sleep(0.5)
            """
            try:
                is_request = self.gui.getIsRequest()
                if is_request:
                    self.gui.turnOffIsRequest()
                with grpc.insecure_channel('localhost:50060') as channel:
                    stub = services_pb2_grpc.InformationStub(channel)
                    response = stub.SendHour(empty_pb2.Empty())
                    self.queue.put(response.hour)

                    if is_request:
                        print("fdsafdsafdsafdsa")
                        response2 = stub.SendBook(empty_pb2.Empty())
                        self.queue.put(response2.book)
                        print(response2)
                    print(response.hour)
                    sys.stdout.flush()
            except:
                print("Error trying to do that1")
            time.sleep(1)

root = tkinter.Tk()
client = Aplication(root)
root.mainloop()
