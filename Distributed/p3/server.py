# -*- coding: utf-8 -*-
import sys
import os
import tkinter
import tools
import time
import threading
import random
import queue
import dbtools as db
from PIL import ImageTk, Image
#This is the server part
from socket import *
myHost = ''
myPort = 50007


class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.queue = queue
        self.master = master

        self.isEditable_1 = False
        self.isEditable_2 = False
        self.isEditable_3 = False
        self.isEditable_4 = False

        self.isSet_1 = False
        self.isSet_2 = False
        self.isSet_3 = False
        self.isSet_4 = False

        self.isReset = False

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

        self.set_1 = tkinter.Button(master, text='Enviar', command=lambda: self.OnSet(1), width=10)
        self.set_2 = tkinter.Button(master, text='Enviar', command=lambda: self.OnSet(2), width=10)
        self.set_3 = tkinter.Button(master, text='Enviar', command=lambda: self.OnSet(3), width=10)
        self.set_4 = tkinter.Button(master, text='Enviar', command=lambda: self.OnSet(4), width=10)

        img_none = self.createImage("na.jpg")
        self.book_image = tkinter.Label(master, image=img_none, text="Grafica1")
        self.book_image.image = img_none

        self.end = tkinter.Button(master, text='Done', command=endCommand, width=10)
        self.reset = tkinter.Button(master, text='Reiniciar', state="disabled", command=lambda: self.resetButton(), width=10)

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

        self.book_image.grid(row=4, column=1)

        self.end.grid(row=5, column=2)
        self.reset.grid(row=5,column=3)

    def resetButton(self):
        self.isReset = True
        self.reset["state"] = "disabled"

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

    def createEmptyPopup(self):
        top = tkinter.Toplevel()
        top.title("Alerta")
        msg = tkinter.Message(top, text="Ya no hay libros, presione el botón REINICIAR")
        msg.pack()

        button = tkinter.Button(top, text="Aceptar", command=top.destroy)
        button.pack()

    def createImage(self, path):
        return ImageTk.PhotoImage(Image.open(path))

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

        #Database
        self.databaseConnection = db.Database()
        self.books = self.databaseConnection.selectAllBooks()
        self.shuffleBooks()
        self.counter_books = 0
        self.isBackup = True

        #Set up the network part
        self.socket = None 
        self.createConexion()

        self.clock1 = None
        self.clock2 = None
        self.clock3 = None
        self.clock4 = None

        self.counter = -1

        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        self.running = 1

        self.thread1 = threading.Thread(target=self.workerThread, args=[1], daemon=True)
        self.thread1.start()

        self.thread2 = threading.Thread(target=self.workerThread, args=[2], daemon=True)
        self.thread2.start()

        self.thread3 = threading.Thread(target=self.workerThread, args=[3], daemon=True)
        self.thread3.start()

        self.thread4 = threading.Thread(target=self.workerThread, args=[4], daemon=True)
        self.thread4.start()

        self.threadN = threading.Thread(target=self.workerThreadNewtork, daemon=True)
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
            btn_id, is_editeable_btn = self.gui.getEditable(n_thread)
            setattr(self, 'clock' + str(n_thread), current_time)
            if is_editeable_btn and btn_id == n_thread:
               pass
            else:
                if self.gui.getSeteable(btn_id):
                    current_time = self.gui.getTextFromEditable(btn_id)
                    self.gui.turnOffSet(btn_id)
                else:
                    current_time = tools.generateNextTime(current_time)
            self.queue.put(str(n_thread) + "|" + current_time)

    def workerThreadNewtork(self):
        while self.running:
            connection, address = self.sockobj.accept()
            print('Server connected by', address)
            self.databaseConnection.insertIntoUser(str(address[0]))
            self.isBackup = True
            hn = threading.Thread(target=self.handleClient, args=[connection], daemon=True)
            hn.start()

    def handleClient(self, connection): 
        self.counter += 1
        if self.counter > 5: self.counter = 1
        local_id = self.counter

        #backup server
        if not self.counter:
            while True:
                if self.isBackup:
                    self.databaseConnection.exportDatabase()
                    connection.send(str(os.path.getsize('dump.sql')).encode())
                    data = connection.recv(1024)
                    file = 'dump.sql'
                    f = open(file, 'rb')
                    l = f.read(1024)
                    while(l):
                        connection.send(l)
                        l = f.read(1024)
                    f.close
                    print('Done sending')
                    self.isBackup = False

        else:
            while True:
                data = connection.recv(1024)
                request_book = int(data.decode())

                if self.gui.isReset:
                    self.shuffleBooks()
                    self.counter_books = 0
                    self.gui.isReset = False

                if request_book:
                    if self.counter_books == len(self.books)-1:
                        self.gui.reset['state'] = "normal"
                        self.gui.createEmptyPopup()
                        new_image =  self.gui.createImage("na.jpg")
                        self.gui.book_image.config(image = new_image)
                        self.gui.book_image.image =new_image
                        connection.send(str(local_id).encode() + br"_" + self.getClock(local_id).encode() + br"_" + br"00")
                    else:
                        selected_book = self.books[self.counter_books]
                        connection.send(str(local_id).encode() + br"_" + self.getClock(local_id).encode() + br"_" + selected_book.encode() + br"_" + br"data")
                        new_image =  self.gui.createImage(self.books[self.counter_books].split(",")[-1])
                        self.gui.book_image.config(image = new_image)
                        self.gui.book_image.image =new_image
                        self.counter_books += 1
                        self.databaseConnection.insertDetail(connection.getpeername()[0],selected_book[0])
                        self.isBackup = True
                else:
                    connection.send(str(local_id).encode() + br"_" + self.getClock(local_id).encode())
                if not data: break
        connection.close()

    def endApplication(self):
        self.running = 0

    def getClock(self, number):
        return getattr(self, 'clock' + str(number))

    def shuffleBooks(self):
        random.shuffle(self.books)

    def createConexion(self):
        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.bind((myHost, myPort))
        self.sockobj.listen(6)


rand = random.Random(  )

#tinker
root = tkinter.Tk()
client = Aplication(root)
root.mainloop()