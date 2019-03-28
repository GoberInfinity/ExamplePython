import sys, os
sys.path.append(os.path.abspath(os.path.join('../..', 'tools')))
sys.path.append(os.path.abspath(os.path.join('../..', 'gui')))
import servergui, tkinter
import timer, time
import threading, queue

from socket import *
myHost = ''
myPort = 50007

class Aplication:
    def __init__(self, master):
        self.master = master
        self.queue = queue.Queue()

        self.gui = servergui.GuiPart(master, self.queue)

        self.socket = None
        self.counter = 0
        self.createConexion()

        self.clock1 = None
        self.clock2 = None
        self.clock3 = None
        self.clock4 = None

        self.thread1 = threading.Thread(target=self.workerThread, args=[1], daemon=True).start()
        self.thread2 = threading.Thread(target=self.workerThread, args=[2], daemon=True).start()
        self.thread3 = threading.Thread(target=self.workerThread, args=[3], daemon=True).start()
        self.thread4 = threading.Thread(target=self.workerThread, args=[4], daemon=True).start()
        self.threadN = threading.Thread(target=self.workerThreadNewtork, daemon=True).start()

        self.periodicCall()

    def periodicCall(self):
        self.gui.processIncoming()
        self.master.after(100, self.periodicCall)

    def workerThread(self, n_thread):
        if n_thread == 1:
            current_time = timer.getCurrentTime()
        else:
            current_time = timer.getRandomTime()

        while True:
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
                    current_time = timer.generateNextTime(current_time)
            self.queue.put(str(n_thread) + "|" + current_time)

    def createConexion(self):
        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.bind((myHost, myPort))
        self.sockobj.listen(5)

    def workerThreadNewtork(self):
        while True:
            connection, address = self.sockobj.accept()
            sys.stdout.flush()
            print('Server connected by', address)
            hn = threading.Thread(target=self.handleClient, args=[connection], daemon=True).start()

    def handleClient(self, connection):
        self.counter += 1
        if self.counter > 5: self.counter = 1
        local_id = self.counter
        while True:
            data = connection.recv(1024)
            if not data: break
            connection.send(br'Echo=>' + self.getClock(local_id).encode())
        connection.close()

    def getClock(self, number):
        return getattr(self, 'clock' + str(number))

root = tkinter.Tk()
client = Aplication(root)
root.mainloop()