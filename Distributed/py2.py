# -*- coding: utf-8 -*-

import tkinter
import tools
import time
import threading
import random
import queue

class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        
        self.isEditable_1 = False
        self.isEditable_2 = False
        self.isEditable_3 = False
        self.isEditable_4 = False
        
        self.isSet_1 = False
        self.isSet_2 = False
        self.isSet_3 = False
        self.isSet_4 = False
               
        # Set up the GUI
        self.txt_clock_1 = tkinter.Label(master, text='', width=20)
        self.txt_clock_2 = tkinter.Label(master, text='', width=20)
        self.txt_clock_3 = tkinter.Label(master, text='', width=20)
        self.txt_clock_4 = tkinter.Label(master, text='', width=20)
        
        self.input_clock_1 = tkinter.Entry(master, text='', width=40)
        self.input_clock_2 = tkinter.Entry(master, text='', width=40)
        self.input_clock_3 = tkinter.Entry(master, text='', width=40)
        self.input_clock_4 = tkinter.Entry(master, text='', width=40)
        
        self.edit_1 = tkinter.Button(master, text='Editar', command=lambda: self.OnEdit(1), width=10)
        self.edit_2 = tkinter.Button(master, text='Editar', command=lambda: self.OnEdit(2), width=10)
        self.edit_3 = tkinter.Button(master, text='Editar', command=lambda: self.OnEdit(3), width=10)
        self.edit_4 = tkinter.Button(master, text='Editar', command=lambda: self.OnEdit(4), width=10)
        
        self.set_1 = tkinter.Button(master, text='Settear', command=lambda: self.OnSet(1), width=10)
        self.set_2 = tkinter.Button(master, text='Settear', command=lambda: self.OnSet(2), width=10)
        self.set_3 = tkinter.Button(master, text='Settear', command=lambda: self.OnSet(3), width=10)
        self.set_4 = tkinter.Button(master, text='Settear', command=lambda: self.OnSet(4), width=10)
        
        self.end = tkinter.Button(master, text='Done', command=endCommand, width=20)
        
        self.txt_clock_1.grid(row=0, column=0)
        self.txt_clock_2.grid(row=1, column=0)
        self.txt_clock_3.grid(row=2, column=0)
        self.txt_clock_4.grid(row=3, column=0)
        
        self.input_clock_1.grid(row=0, column=1)
        self.input_clock_2.grid(row=1, column=1)
        self.input_clock_3.grid(row=2, column=1)
        self.input_clock_4.grid(row=3, column=1)
        
        self.edit_1.grid(row=0, column=2)
        self.edit_2.grid(row=1, column=2)
        self.edit_3.grid(row=2, column=2)
        self.edit_4.grid(row=3, column=2)
        
        self.set_1.grid(row=0, column=3)
        self.set_2.grid(row=1, column=3)
        self.set_3.grid(row=2, column=3)
        self.set_4.grid(row=3, column=3)
        
        self.end.grid(row=4, column=0)
        
    def OnEdit(self, button_id):
        setattr(self, 'isEditable_' + str(button_id), True)
        setattr(self, 'isSet_' + str(button_id), False)
            
    def OnSet(self, button_id):
        setattr(self, 'isEditable_' + str(button_id), False)
        setattr(self, 'isSet_' + str(button_id), True)
           
    def getEditable(self, number):
        return number, getattr(self, 'isEditable_' + str(number))
    
    def getSeteable(self, number):
        return getattr(self, 'isSet_' + str(number))

    def getTextFromEditable(self, number):
         return getattr(self, 'input_clock_' + str(number)).get()
    
    def turnOffSet(self, number):
        setattr(self, 'isSet_' + str(number), False)
        att = getattr(self, "input_clock_" + str(number))
        att.delete(0, 'end')
        
    def processIncoming(self):
        """Handle all messages currently in the queue, if any."""
        while self.queue.qsize():
            try:
                msg = self.queue.get(0).split("|")
                if msg[0] == "1":
                    self.txt_clock_1["text"] = msg
                elif msg[0] == "2":
                    self.txt_clock_2["text"] = msg
                elif msg[0] == "3":
                    self.txt_clock_3["text"] = msg
                else:
                    self.txt_clock_4["text"] = msg
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
            # To simulate asynchronous I/O, we create a random number at
            # random intervals. Replace the following two lines with the real
            # thing.
            time.sleep(1)
            btn_id, is_editeable_btn = self.gui.getEditable(n_thread)
            if is_editeable_btn and btn_id == n_thread:
               pass              
            else:
                if self.gui.getSeteable(btn_id):
                    current_time = self.gui.getTextFromEditable(btn_id)
                    self.gui.turnOffSet(btn_id)
                    print(f"This is thread {n_thread} and is editable")
                else:
                    current_time = tools.generateNextTime(current_time)
            self.queue.put(str(n_thread) + "|" + current_time)
            
    def endApplication(self):
        self.running = 0


rand = random.Random(  )

#tinker
root = tkinter.Tk()
client = Aplication(root)
root.mainloop()