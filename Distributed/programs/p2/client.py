import sys, os
sys.path.append(os.path.abspath(os.path.join('../..', 'gui')))
import tkinter, clientgui
import time, threading, queue

from socket import *
serverHost = 'localhost'
serverPort = 50007

class Aplication:
    def __init__(self, master):

        self.master = master
        self.queue = queue.Queue()
        self.gui =  clientgui.GuiPart(master, self.queue)

        #Set up the network part
        self.socket = None
        self.createConexion()

        self.thread1 = threading.Thread(target=self.workerThreadNewtork, daemon=True).start()
        self.periodicCall()

    def periodicCall(self):
        self.gui.processIncoming()
        self.master.after(100, self.periodicCall)

    def workerThreadNewtork(self):
        while True:
            message = [b'Hello network world']
            self.sockobj.send(message[0])
            data = self.sockobj.recv(1024)
            self.queue.put(data)
            time.sleep(0.5)

    def createConexion(self):
        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.connect((serverHost, serverPort))

root = tkinter.Tk()
client = Aplication(root)
root.mainloop()