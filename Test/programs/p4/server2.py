import sys, os
sys.path.append(os.path.abspath(os.path.join('../..', 'tools')))
sys.path.append(os.path.abspath(os.path.join('../..', 'gui')))
import servergui, tkinter
import timer, time
import threading, queue, random
import database, json

from socket import *
myHost = 'localhost'
myPort = 50010
CHUNK_SIZE = 8 * 1024

database_location = "../../data/seconddb/s_db.db"
database_script_location = '../../data/seconddb/dump.sql'
database_recieved_script_location = "../../data/seconddb/dumped.sql"

class Aplication:
    def __init__(self, master):
        self.master = master
        self.queue = queue.Queue()

        self.gui = servergui.GuiPart(master, self.queue)

        self.socket = None
        self.createConexion()

        self.clock1 = None
        self.clock2 = None
        self.clock3 = None
        self.clock4 = None

        #Database
        self.databaseConnection = database.Database(database_location)
        self.books = self.databaseConnection.selectAllBooks()
        self.shuffleBooks()
        self.counter_books2 = 0

        self.counter = 0
        self.isSelfRest = 0
        self.isBackup = True
        self.firstConecction = True

        self.thread1 = threading.Thread(target=self.workerThread, args=[1], daemon=True).start()
        self.thread2 = threading.Thread(target=self.workerThread, args=[2], daemon=True).start()
        self.thread3 = threading.Thread(target=self.workerThread, args=[3], daemon=True).start()
        self.thread4 = threading.Thread(target=self.workerThread, args=[4], daemon=True).start()
        self.thread5 = threading.Thread(target=self.replicaThread, daemon=True).start()
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
        self.sockobj.listen(6)

    def workerThreadNewtork(self):
        while True:
            connection, address = self.sockobj.accept()
            sys.stdout.flush()
            print('Server connected by', address)
            self.databaseConnection.insertIntoUser(str(address[0]))
            self.isBackup = True
            hn = threading.Thread(target=self.handleClient, args=[connection], daemon=True).start()

    def handleClient(self, connection):
        self.counter += 1
        if self.counter > 5: self.counter = 1
        local_id = self.counter

        #backup server
        if not self.counter:
            pass
        else:
            while True:

                if self.gui.isReset:
                    self.shuffleBooks()
                    self.counter_books2 += 1
                    self.gui.isReset = False
                    self.isSelfRest = 1

                data = connection.recv(1024)
                request_book = int(data.decode())

                if request_book:
                    if self.counter_books2 == len(self.books)-1:
                        self.gui.reset['state'] = "normal"
                        self.gui.createEmptyPopup()
                        new_image =  self.gui.createImage("../../images/na.jpg")
                        self.gui.book_image.config(image = new_image)
                        self.gui.book_image.image =new_image
                        connection.send(str(local_id).encode() + br"_" + self.getClock(local_id).encode() + br"_" + br"00")
                    else:
                        selected_book = self.books[self.counter_books2]
                        connection.send(str(local_id).encode() + br"_" + self.getClock(local_id).encode() + br"_" + selected_book.encode() + br"_" + br"data")
                        new_image =  self.gui.createImage("../../images/" + self.books[self.counter_books2].split(",")[-1])
                        self.gui.book_image.config(image = new_image)
                        self.gui.book_image.image =new_image
                        self.counter_books2 += 1
                        self.databaseConnection.insertDetail(connection.getpeername()[0],selected_book[0])
                        self.isBackup = True
                else:
                    connection.send(str(local_id).encode() + br"_" + self.getClock(local_id).encode())
                if not data: break
        connection.close()

    def getClock(self, number):
        return getattr(self, 'clock' + str(number))

    def shuffleBooks(self):
        random.shuffle(self.books)

    def replicaThread(self):
        serverHost = 'localhost'
        serverPort = 50007
        CHUNK_SIZE = 8 * 1024
        connection = socket(AF_INET, SOCK_STREAM)
        connection.connect((serverHost, serverPort))
        while True:
            #We recieve the array information
            data2 = connection.recv(1024)
            data2 = json.loads(data2.decode())

            #We recieve the information about the other server
            data = json.dumps({"a": self.books, 'b': self.counter_books2, 'c':self.isSelfRest})
            connection.send(data.encode())

            #We send if our server changed
            server1changed = int(connection.recv(1024).decode())
            server2changed = int(self.isBackup)
            connection.send(str(server2changed).encode())

            #print(f"Server 1 {server1changed} - Server 2 {server2changed}")
            print(f"Server2 recieved1 =  {data2['c']} counter of server1 {data2['b']} currentCounter {self.counter_books2} ")
            sys.stdout.flush()

            #If server2 changed recieve the file
            if server1changed:
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
                            terminated = True
                            break
                self.databaseConnection.closeConnection()
                os.remove(database_location)
                os.system('cat '+ database_recieved_script_location  + ' | sqlite3 ' + database_location)
                print("CREATED")
                self.databaseConnection.createConnection(database_location)
                connection.send(b"Recieved")

            #If server1 changes send the file
            if server2changed:
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

            counter_server1 = int(data2['b'])
            is_other_server_reseted = int(data2['c'])

            if self.firstConecction:
                self.books = data2['a']
                self.firstConecction = False

            if counter_server1 == 7:
                self.books = data2['a']
                self.counter_books2 = 0
                counter_server1 = 0

            if(counter_server1 == 7 and self.counter_books2 == 0) or (counter_server1 == 0 and self.counter_books2 == 7) or (counter_server1 == 1 and self.counter_books2 == 7):
                self.counter_books2 = 0
                self.isSelfRest = 0
            else:
                self.counter_books2 = max(self.counter_books2, counter_server1)
            time.sleep(0.5)
        connection.close()

root = tkinter.Tk()
client = Aplication(root)
root.mainloop()