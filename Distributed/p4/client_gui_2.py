# -*- coding: utf-8 -*-

import tkinter as tk
import time
import threading
import queue

#This is the server part
from socket import *
serverHost = 'localhost'
serverPort = 50010



class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.queue = queue

        self.is_request = 0
        self.info_data = "Libro"

        # Set up the GUI
        self.ds_clock = tk.Label(master, text='', width=20)
        self.info = tk.Label(master, text=self.info_data, width=80,  padx=10, pady=10)
        self.request = tk.Button(master, text='Solicitar', command=lambda: self.turnOnIsRequest(), width=20)
        self.end = tk.Button(master, text='Salir', command=endCommand, width=20)

        self.ds_clock.grid(row=0, column=0)
        self.info.grid(row=1, column=0)
        self.request.grid(row=2, column=0)
        self.end.grid(row=3, column=0)
    
    def createEmptyPopup(self):
        top = tk.Toplevel()
        top.title("Alerta")
        msg = tk.Message(top, text="Ya no hay libros disponibles")
        msg.pack()

        button = tk.Button(top, text="Aceptar", command=top.destroy)
        button.pack()

    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize():
            try:
                msg = self.queue.get(0).decode().split("_")
                print(msg)
                if len(msg) == 3:
                    self.createEmptyPopup()
                elif len(msg) == 4:
                    print("We´re reciving data")
                    book_data = msg[2].split(",")
                    name = "Nombre: " + book_data[1]
                    autor = "Autor: " + book_data[2]
                    editorial = "Editorial: " + book_data[3]
                    precio = "Precio: " + book_data[4]
                    self.info_data = name + ' ' + autor + ' ' + editorial + ' ' + precio
                self.ds_clock["text"] = msg[1]
                self.info["text"] = self.info_data
            except queue.Empty:
                pass

    def getIsRequest(self):
        return getattr(self, 'is_request')

    def turnOffIsRequest(self):
        setattr(self, 'is_request', 0)

    def turnOnIsRequest(self):
        setattr(self, 'is_request', 1)

class Aplication:
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well. We spawn a new thread for the worker (I/O).
        """
        self.master = master
        self.queue = queue.Queue()
        self.counter = 0
        self.socket = None
        self.client_number = -1

        # Set up the GUI part
        self.gui = GuiPart(master, self.queue, self.endApplication)

        #Set up the network part
        self.createConnetion()

        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = 1

        self.thread1 = threading.Thread(target=self.workerThreadNewtork, daemon=True)
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
            is_editable = self.gui.getIsRequest()
            message = [str(is_editable).encode()]
            if is_editable:
                self.gui.turnOffIsRequest()

            self.sockobj.send(message[0])

            data = self.sockobj.recv(1024)
            self.queue.put(data)
            self.counter +=1
            time.sleep(0.5)

    def endApplication(self):
        self.running = 0

    def createConnetion(self):
        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.connect((serverHost, serverPort))


#tinker
root = tk.Tk()
client = Aplication(root)
root.mainloop()