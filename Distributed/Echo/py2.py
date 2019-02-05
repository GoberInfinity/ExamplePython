# -*- coding: utf-8 -*-

import tkinter
import tools
import time
import threading
import random
import queue

#This is the server part
from socket import *
myHost = '' 
myPort = 50007

class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        
        self.isEditable_1 = False
        self.isEditable_2 = False
        self.isEditable_3 = False
        self.isEditable_4 = False
               
        # Set up the GUI
        self.fs_txt_clock = tkinter.Label(master, text='', width=20)
        self.sd_txt_clock = tkinter.Label(master, text='', width=20)
        self.td_txt_clock = tkinter.Label(master, text='', width=20)
        self.ft_txt_clock = tkinter.Label(master, text='', width=20)
        
        self.fs_input_clock = tkinter.Entry(master, text='', width=40)
        self.sd_input_clock = tkinter.Entry(master, text='', width=40)
        self.td_input_clock = tkinter.Entry(master, text='', width=40)
        self.ft_input_clock = tkinter.Entry(master, text='', width=40)
        
        self.fs_edit_btn = tkinter.Button(master, text='Editar', command=lambda: self.OnButtonClick(1), width=10)
        self.sd_edit_btn = tkinter.Button(master, text='Editar', command=lambda: self.OnButtonClick(2), width=10)
        self.td_edit_btn = tkinter.Button(master, text='Editar', command=lambda: self.OnButtonClick(3), width=10)
        self.ft_edit_btn = tkinter.Button(master, text='Editar', command=lambda: self.OnButtonClick(4), width=10)
        
        self.end = tkinter.Button(master, text='Done', command=endCommand, width=20)
        
        self.fs_txt_clock.grid(row=0, column=0)
        self.sd_txt_clock.grid(row=1, column=0)
        self.td_txt_clock.grid(row=2, column=0)
        self.ft_txt_clock.grid(row=3, column=0)
        
        self.fs_input_clock.grid(row=0, column=1)
        self.sd_input_clock.grid(row=1, column=1)
        self.td_input_clock.grid(row=2, column=1)
        self.ft_input_clock.grid(row=3, column=1)
        
        self.fs_edit_btn.grid(row=0, column=2)
        self.sd_edit_btn.grid(row=1, column=2)
        self.td_edit_btn.grid(row=2, column=2)
        self.ft_edit_btn.grid(row=3, column=2)
        
        self.end.grid(row=4, column=0)
        
    def OnButtonClick(self, button_id):
        if button_id == 1:
            self.isEditable_1 = not self.isEditable_1
        elif button_id == 2:
            self.isEditable_2 = not self.isEditable_2
        elif button_id == 3:
            self.isEditable_3 = not self.isEditable_3
        else:
            self.isEditable_4 = not self.isEditable_4
            
    def getEditable(self, number):
        return number, getattr(self, 'isEditable_' + str(number))
    
    def getTextFromEditable(self, number):
        if number == 1:
            return self.fs_input_clock.get()
        elif number == 2:
            return self.sd_input_clock.get()
        elif number == 3:
            return self.td_input_clock.get()
        else:
            return self.ft_input_clock.get()
        

    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize():
            try:
                msg = self.queue.get(0).split("|")
                if msg[0] == "1":
                    self.fs_txt_clock["text"] = msg
                elif msg[0] == "2":
                    self.sd_txt_clock["text"] = msg
                elif msg[0] == "3":
                    self.td_txt_clock["text"] = msg
                else:
                    self.ft_txt_clock["text"] = msg
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
        
        self.originalClock = None

        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = 1
        
        self.thread1 = threading.Thread(target=self.workerThread, args=[1])
        self.thread1.start()

        self.thread2 = threading.Thread(target=self.workerThread, args=[2])
        self.thread2.start()
        
        self.thread3 = threading.Thread(target=self.workerThread, args=[3])
        self.thread3.start()
        
        self.thread4 = threading.Thread(target=self.workerThread, args=[4])
        self.thread4.start()
        
        self.threadN = threading.Thread(target=self.workerThreadNewtork)
        self.threadN.start()

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
        self.master.after(100, self.periodicCall)

    def workerThread(self, n_thread):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select(  )'. One important thing to remember is that the thread has
        to yield control pretty regularly, by select or otherwise.
        """
        print(f"This is the new thread {n_thread}")
        if n_thread == 1:
            current_time = tools.getCurrentTime()
        else:
            current_time = tools.getRandomTime()
        
        while self.running:
            time.sleep(1)
            btn_id, is_editable_btn = self.gui.getEditable(n_thread)
            
            if n_thread == 1:
                self.originalClock = current_time
            
            if is_editable_btn and btn_id == n_thread:
                current_time = self.gui.getTextFromEditable(btn_id)
                print(f"This is thread {n_thread} and is editable")
            else:
                current_time = tools.generateNextTime(current_time)
            self.queue.put(str(n_thread) + "|" + current_time)
            
    def workerThreadNewtork(self):
        while self.running:
                connection, address = self.sockobj.accept()   
                print('Server connected by', address)
                while True:
                    data = connection.recv(1024)        
                    if not data: break 
                    connection.send(br'Echo=>' + self.originalClock.encode())
                connection.close()
                    
    def endApplication(self):
        self.running = 0
        
    def createConexion(self):
        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.bind((myHost, myPort))
        self.sockobj.listen(5)


rand = random.Random(  )

#tinker
root = tkinter.Tk()
client = Aplication(root)
root.mainloop()