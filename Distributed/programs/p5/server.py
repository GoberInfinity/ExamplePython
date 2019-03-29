#python server.py 50070 10:50060 0 ../../data/seconddb/dump.sql ../../data/s2froms1.sql ../../data/seconddb/s_db.db
#python server.py 50060 localhost:50070,localhost:50080 0 ../../data/firstdb/dump.sql ../../data/s1fromsn.sql ../../data/firstdb/f_db.db

from __future__ import print_function
from concurrent import futures
from google.protobuf import empty_pb2

import operator
import sys, os
import logging, grpc

sys.path.append(os.path.abspath(os.path.join('../..', 'tools')))
sys.path.append(os.path.abspath(os.path.join('../..', 'gui')))
sys.path.append(os.path.abspath(os.path.join('../..', 'protos')))

import services_pb2, services_pb2_grpc
import servergui, tkinter, fchunk
import timer, time, conection
import threading, queue, random
import database

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


database_location = "../../data/firstdb/f_db.db"
database_script_location = '../../data/firstdb/dump.sql'
database_recieved_script_location = "../../data/firstdb/dumped.sql"

g_book_counter = -1
g_books = []
g_hour = ""
g_book = ""

g_needs_restore = False
g_update_book_gui = False
g_empty_books = False

g_path_of_watched_file = None
g_path_of_replica_file = None
g_path_of_database = None

g_last_ip = ""


class Services(services_pb2_grpc.InformationServicer):

    def SendCounter(self, request, context):
        self.__reset_counter()
        return services_pb2.CounterReply(counter = g_book_counter)

    def SendBooks(self, request, context):
        return services_pb2.BooksReply(books = '_'.join(g_books))

    def SendHour(self, request, context):
        return services_pb2.HourReply(hour = g_hour)

    def SendBook(self, request, context):
        self.__setLastIp(context)
        return services_pb2.BookReply(book = self.__get_new_book())

    def SendDB(self, request, unused_context):
        self.__createScriptBeforeSend()
        return fchunk.chunk_bytes(g_path_of_watched_file)

    def __createScriptBeforeSend(self):
        while g_update_book_gui:
            time.sleep(0.1)
        databaseConnection = database.Database(g_path_of_database)
        databaseConnection.exportDatabase(g_path_of_watched_file)
        databaseConnection.closeConnection()

    def __setLastIp(self, context):
        global g_last_ip
        metadata = dict(context.invocation_metadata())
        g_last_ip = metadata['ip']

    def __reset_counter(self):
        global g_needs_restore, g_book_counter
        if g_needs_restore:
            g_book_counter = -1
            g_needs_restore = False

    def __get_new_book(self):
        global g_book_counter, g_empty_books
        book_reply = 'None'
        if g_book_counter < len(g_books)-1:
            g_book_counter += 1
            book_reply = g_books[g_book_counter]
        else:
            g_empty_books = True
        self.__update_gui()
        return book_reply

    def __update_gui(self):
        global g_update_book_gui
        g_update_book_gui = True

class Aplication:
    def __init__(self, master):
        self.master = master
        self.queue = queue.Queue()

        self.gui = servergui.GuiPart(master, self.queue)

        self.clock1 = None
        self.clock2 = None
        self.clock3 = None
        self.clock4 = None

        #Server configurations
        self.port = str(sys.argv[1])
        self.servers = (str(sys.argv[2])).split(',')
        self.master_server = int(sys.argv[3])
        self.setFilePaths()

        self.servers_responses_counter = [-10 for _ in range(len(self.servers))]

        #Database
        self.databaseConnection = database.Database(g_path_of_database)
        self.books = self.databaseConnection.selectAllBooks()
        self.shuffleBooks()
        self.counter_books = 0

        self.thread1 = threading.Thread(target=self.workerThread, args=[1], daemon=True).start()
        self.thread2 = threading.Thread(target=self.workerThread, args=[2], daemon=True).start()
        self.thread3 = threading.Thread(target=self.workerThread, args=[3], daemon=True).start()
        self.thread4 = threading.Thread(target=self.workerThread, args=[4], daemon=True).start()
        self.thread5 = threading.Thread(target=self.updateGUI, daemon=True).start()

        self.thread6 = threading.Thread(target=self.serve).start()
        self.thread7 = threading.Thread(target=self.consume).start()

        self.periodicCall()

    def setFilePaths(self):
        global g_path_of_watched_file, g_path_of_replica_file, g_path_of_database
        g_path_of_watched_file = str(sys.argv[4])
        g_path_of_replica_file = str(sys.argv[5])
        g_path_of_database = str(sys.argv[6])

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
        global g_update_book_gui, g_empty_books, g_book_counter, g_needs_restore
        ips = set()

        while True:

            if self.gui.isReset:
                g_empty_books = False
                self.shuffleBooks()
                self.gui.isReset = False
                g_needs_restore = True

            if g_update_book_gui:
                if g_empty_books:
                        self.gui.reset['state'] = "normal"
                        self.gui.createEmptyPopup()
                        new_image =  self.gui.createImage("../../images/na.jpg")
                        self.gui.book_image.config(image = new_image)
                        self.gui.book_image.image =new_image
                else:
                    selected_book = g_books[g_book_counter]
                    new_image =  self.gui.createImage("../../images/" + g_books[g_book_counter].split(",")[-1])
                    self.gui.book_image.config(image = new_image)
                    self.gui.book_image.image = new_image
                    if g_last_ip not in ips:
                        ips.add(g_last_ip)
                        self.databaseConnection.insertIntoUser(g_last_ip)
                    self.databaseConnection.insertDetail(g_last_ip,selected_book[0])
                g_update_book_gui = False
            time.sleep(0.5)

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

    def consume(self):
        global g_book_counter, g_books
        server1 = self.servers[0].split(':')
        ip_server = server1[0]
        port_server = server1[1]
        first_time = True

        while True:
            other_servers_counter = -2
            something_changed = False
            restarted_server = None
            self.servers_responses_counter = []

            #get first data from master
            if first_time and not self.master_server:
                print("Sync from first time")
                try:
                    b_response = conection.callService('GetBooks','localhost',str(port_server))
                    g_books = (b_response.books).split('_')
                    print(f"Books SINKED {g_books}")
                    sys.stdout.flush()
                    first_time = False
                    something_changed = True
                except:
                    print("Error trying to get the books")
                    sys.stdout.flush()

            for server in self.servers:
                server_data = server.split(':')
                ip_server = str(server_data[0])
                port_server = str(server_data[1])

                #get all the counters from the other servers, if you cannot get the response, add -10
                try:
                    c_response = conection.callService('GetCounter',ip_server,port_server)
                    other_servers_counter = c_response.counter
                    self.servers_responses_counter.append(other_servers_counter)
                    print(c_response.counter)
                    sys.stdout.flush()
                except:
                    self.servers_responses_counter.append(-10)
                    print("Error trying to get the counter S1")
                    sys.stdout.flush()

            print(self.servers_responses_counter)
            sys.stdout.flush()
            #get the maximum index
            index_of_max_in_other_server, max_in_other_server = max(enumerate(self.servers_responses_counter), key=operator.itemgetter(1))

            reset_in_other_server = -1 in self.servers_responses_counter

            if reset_in_other_server and g_book_counter == -1:
                time.sleep(1)
                continue

            #Only triggers when a server needs to restart the books
            if reset_in_other_server and g_book_counter == len(g_books)-1:
                g_book_counter = -1
                print("Server restarted")
                sys.stdout.flush()
                restarted_server = self.servers_responses_counter.index(-1)
                data_ser = self.servers[restarted_server].split(':')
                #Get the new book from the server that was the lowest key
                try:
                    br_response = conection.callService('GetBooks',data_ser[0],data_ser[1])
                    g_books = (br_response.books).split('_')
                    print(g_books)
                    sys.stdout.flush()
                except:
                    print("Error trying to get the books")
                    sys.stdout.flush()
                something_changed = True
            elif max_in_other_server == -1 and first_time:
                pass
            elif max_in_other_server > g_book_counter:
                print("Server needs to update")
                sys.stdout.flush()
                g_book_counter = max_in_other_server
                something_changed = True

            #Triggers when you have to dowload the lastest data from the server that changed
            if something_changed:
                if not restarted_server:
                    restarted_server = index_of_max_in_other_server
                data_ser = self.servers[restarted_server].split(':')
                print(f"Gettinf information from {data_ser}")
                sys.stdout.flush()
                try:
                    f_response = conection.callService('GetFile',data_ser[0],data_ser[1])
                    f = open(g_path_of_replica_file, 'wb')
                    f.write(f_response)
                    f.close()
                    self.createNewDatabase()
                    sys.stdout.flush()
                except:
                    print("Error trying to get the file")
                    sys.stdout.flush()
                print("Server updated")
                sys.stdout.flush()
                something_changed = False
            time.sleep(1)


    def getClock(self, number):
        return getattr(self, 'clock' + str(number))

    def shuffleBooks(self):
        random.shuffle(self.books)
        global g_books
        g_books = self.books

    def createNewDatabase(self):
        self.databaseConnection.closeConnection()
        os.remove(g_path_of_database)
        os.system('cat ' + g_path_of_replica_file + ' | sqlite3 ' + g_path_of_database)
        self.databaseConnection.createConnection(g_path_of_database)
        print("Database Created")

root = tkinter.Tk()
client = Aplication(root)
root.mainloop()