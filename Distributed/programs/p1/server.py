# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.abspath(os.path.join('../..', 'tools')))
sys.path.append(os.path.abspath(os.path.join('../..', 'gui')))
import servergui, tkinter
import timer, time
import threading, queue

class Aplication:
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI as well. We spawn a new thread for the worker (I/O).
        """
        self.master = master
        self.queue = queue.Queue()

        self.gui = servergui.GuiPart(master, self.queue)

        self.thread1 = threading.Thread(target=self.workerThread, args=[1], daemon=True).start()
        self.thread2 = threading.Thread(target=self.workerThread, args=[2], daemon=True).start()
        self.thread3 = threading.Thread(target=self.workerThread, args=[3], daemon=True).start()
        self.thread4 = threading.Thread(target=self.workerThread, args=[4], daemon=True).start()

        self.periodicCall()

    def periodicCall(self):
        """
        Check every 200 ms if there is something new in the queue.
        """
        self.gui.processIncoming()
        self.master.after(100, self.periodicCall)

    def workerThread(self, n_thread):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select(  )'. One important thing to remember is that the thread has
        to yield control pretty regularly, by select or otherwise.
        """
        if n_thread == 1:
            current_time = timer.getCurrentTime()
        else:
            current_time = timer.getRandomTime()

        while True:
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
                else:
                    current_time = timer.generateNextTime(current_time)
            self.queue.put(str(n_thread) + "|" + current_time)

root = tkinter.Tk()
client = Aplication(root)
root.mainloop()