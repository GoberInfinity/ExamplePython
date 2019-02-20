# -*- coding: utf-8 -*-

import tkinter
import tools
import time
import threading
import random
import queue

#This is the server part
from socket import *
serverHost = '192.168.1.67'
serverPort = 50007

class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
             
        # Set up the GUI
        self.ds_clock = tkinter.Label(master, text='', width=20)
        self.end = tkinter.Button(master, text='Done', command=endCommand, width=20)
        
        self.ds_clock.grid(row=0, column=0)       
        self.end.grid(row=1, column=0)

    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                self.ds_clock["text"] = msg
            except queue.Empty:
                pass

class Aplication:
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well. We spawn a new thread for the worker (I/O).
        """
        self.master = master
        self.queue = queue.Queue()

        # Set up the GUI part
        self.gui = GuiPart(master, self.queue, self.endApplication)
        
        #Set up the network part
        self.socket = None 
        self.createConexion()
        
        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = 1
        
        self.thread1 = threading.Thread(target=self.workerThreadNewtork)
        self.thread1.start()

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodicCall()

    def periodicCall(self):
        """
        Check every 200 ms if there is something new in the queue.
        """
        self.gui.processIncoming()
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            global root
            root.destroy()
            sys.exit(1)
            self.socket.close()
        self.master.after(100, self.periodicCall)

    def workerThreadNewtork(self):
        while self.running:
            message = [b'Hello network world']
            self.sockobj.send(message[0])
            data = self.sockobj.recv(1024)
            self.queue.put(data)
            time.sleep(0.5)
                    
    def endApplication(self):
        self.running = 0
        
    def createConexion(self):
        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.connect((serverHost, serverPort))


#tinker
root = tkinter.Tk()
client = Aplication(root)
root.mainloop()