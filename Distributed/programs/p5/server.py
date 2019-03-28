from __future__ import print_function
from concurrent import futures

import sys, os
import logging, grpc

sys.path.append(os.path.abspath(os.path.join('../..', 'tools')))
sys.path.append(os.path.abspath(os.path.join('../..', 'gui')))
sys.path.append(os.path.abspath(os.path.join('../..', 'protos')))

import services_pb2, services_pb2_grpc
import servergui, tkinter
import timer, time
import threading, queue, random
import database

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

database_location = "../../data/firstdb/f_db.db"
database_script_location = '../../data/firstdb/dump.sql'
database_recieved_script_location = "../../data/firstdb/dumped.sql"

g_book_counter = 0
g_books = []
g_hour = ""
g_book = ""

g_update_book_gui = False


class Services(services_pb2_grpc.InformationServicer):
    def SendCounter(self, request, context):
        return services_pb2.CounterReply(counter = g_book_counter)

    def SendBooks(self, request, context):
        return services_pb2.BooksReply(books = ','.join(g_books))

    def SendHour(self, request, context):
        sys.stdout.flush()
        return services_pb2.HourReply(hour = g_hour)

    def SendBook(self, request, context):
        global g_update_book_gui
        g_update_book_gui = True
        metadata = dict(context.invocation_metadata())
        print(metadata)
        return services_pb2.BookReply(book = "Drinking a lot")

    #Missing Chunker

class Aplication:
    def __init__(self, master):
        self.master = master
        self.queue = queue.Queue()

        self.gui = servergui.GuiPart(master, self.queue)

        self.clock1 = None
        self.clock2 = None
        self.clock3 = None
        self.clock4 = None

        #Database
        self.databaseConnection = database.Database(database_location)
        self.books = self.databaseConnection.selectAllBooks()
        self.shuffleBooks()
        self.counter_books = 0

        #Local configuration
        self.is_first_time = 0

        #Server configurations
        self.port = str(sys.argv[1])
        self.servers = (str(sys.argv[2])).split(',')

        print(self.servers)

        """
        self.counter = -1
        self.isSelfRest = 0
        self.isBackup = True
        """

        self.thread1 = threading.Thread(target=self.workerThread, args=[1], daemon=True).start()
        self.thread2 = threading.Thread(target=self.workerThread, args=[2], daemon=True).start()
        self.thread3 = threading.Thread(target=self.workerThread, args=[3], daemon=True).start()
        self.thread4 = threading.Thread(target=self.workerThread, args=[4], daemon=True).start()
        self.thread5 = threading.Thread(target=self.updateGUI, daemon=True).start()

        #thread to server
        self.thread6 = threading.Thread(target=self.serve).start()
        #thread to consume servers


        self.periodicCall()

    def periodicCall(self):
        self.gui.processIncoming()
        self.master.after(100, self.periodicCall)

    def workerThread(self, n_thread):
        global g_hour

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
            if n_thread == 1:
                g_hour = current_time
            self.queue.put(str(n_thread) + "|" + current_time)

    def updateGUI(self):
        global g_update_book_gui
        while True:
            if g_update_book_gui:
                selected_book = self.books[self.counter_books]
                new_image =  self.gui.createImage("../../images/" + self.books[self.counter_books].split(",")[-1])
                self.gui.book_image.config(image = new_image)
                self.gui.book_image.image =new_image
                self.counter_books += 1
                #self.databaseConnection.insertDetail(connection.getpeername()[0],selected_book[0])
                g_update_book_gui = False
            time.sleep(1)

    def serve(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))
        services_pb2_grpc.add_InformationServicer_to_server(Services(), server)
        server.add_insecure_port('[::]:' + self.port)
        server.start()
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)

    """
    def handleClient(self, connection):
        self.counter += 1
        if self.counter > 5: self.counter = 1
        local_id = self.counter

        #backup server
        if not self.counter:
            while True:
                #We send the array information
                data = json.dumps({"a": self.books, 'b': self.counter_books, 'c':self.isSelfRest})
                connection.send(data.encode())
                #We recieve the information about the other server
                data2 = connection.recv(1024)
                data2 = json.loads(data2.decode())

                #We send if our server changed
                server1changed = int(self.isBackup)
                connection.send(str(server1changed).encode())
                server2changed = int(connection.recv(1024).decode())
                print(f"Server1 recievied2  =  {data2['c']}  counter of server2 {data2['b']} ")
                sys.stdout.flush()

                #If server1 changes send the file
                if server1changed:
                    self.databaseConnection.exportDatabase(database_script_location)
                    connection.send(str(os.path.getsize(database_script_location)).encode())
                    data = connection.recv(1024)
                    file = database_script_location
                    f = open(file, 'rb')
                    l = f.read(1024)
                    while(l):
                        connection.send(l)
                        l = f.read(1024)
                    f.close
                    print('Done sending')
                    self.isBackup = False
                    connection.recv(1024)

                #If server2 changed recieve the file
                if server2changed:
                    connection.send(b"Ready to server2")
                    total_size = int(connection.recv(1024).decode())
                    connection.send(b"Ready to recieve")
                    with open(database_recieved_script_location,'wb') as f:
                        print("File opened")
                        size = 0
                        while True:
                            print("Recieveing Data")
                            datan = connection.recv(1024)
                            if not datan: break
                            size += len(datan)
                            f.write(datan)
                            if size == int(total_size):
                                #terminated = True
                                break
                    self.databaseConnection.closeConnection()
                    os.remove(database_location)
                    os.system('cat ' + database_recieved_script_location + ' | sqlite3 ' + database_location)
                    self.databaseConnection.createConnection(database_location)
                    print("CREATED")

                counter_server2 = int(data2['b'])
                is_other_server_reseted = int(data2['c'])

                if counter_server2 == 7:
                    self.books = data2['a']
                    self.counter_books = 0
                    counter_server2 = 0

                if(counter_server2 == 7 and self.counter_books == 0)  or (counter_server2 == 0 and self.counter_books == 7) or (counter_server2 == 1 and self.counter_books == 7):
                    self.counter_books = 0
                    self.isSelfRest = 0
                else:
                    self.counter_books = max(self.counter_books, counter_server2)
        else:
            while True:

                if self.gui.isReset:
                    self.shuffleBooks()
                    self.counter_books += 1
                    self.gui.isReset = False
                    self.isSelfRest = 1

                data = connection.recv(1024)
                request_book = int(data.decode())

                if request_book:
                    if self.counter_books == len(self.books)-1:
                        self.gui.reset['state'] = "normal"
                        self.gui.createEmptyPopup()
                        new_image =  self.gui.createImage("../../images/na.jpg")
                        self.gui.book_image.config(image = new_image)
                        self.gui.book_image.image =new_image
                        connection.send(str(local_id).encode() + br"_" + self.getClock(local_id).encode() + br"_" + br"00")
                    else:
                        selected_book = self.books[self.counter_books]
                        connection.send(str(local_id).encode() + br"_" + self.getClock(local_id).encode() + br"_" + selected_book.encode() + br"_" + br"data")
                        new_image =  self.gui.createImage("../../images/" + self.books[self.counter_books].split(",")[-1])
                        self.gui.book_image.config(image = new_image)
                        self.gui.book_image.image =new_image
                        self.counter_books += 1
                        self.databaseConnection.insertDetail(connection.getpeername()[0],selected_book[0])
                        self.isBackup = True
                else:
                    connection.send(str(local_id).encode() + br"_" + self.getClock(local_id).encode())
                if not data: break
        connection.close()
    """
    def getClock(self, number):
        return getattr(self, 'clock' + str(number))

    def shuffleBooks(self):
        random.shuffle(self.books)


root = tkinter.Tk()
client = Aplication(root)
root.mainloop()