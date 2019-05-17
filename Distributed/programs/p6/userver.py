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
import utcdatabase

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


database_location = "../../data/utcdb/u_db.db"

g_slaves_hour = []

g_book_counter = -1
g_books = []
g_hour = ""
g_book = ""
g_pause = False

g_needs_restore = False
g_update_book_gui = False
g_empty_books = False

g_path_of_watched_file = None
g_path_of_replica_file = None
g_path_of_database = None

g_last_ip = ""
g_data = dict()

class Services(services_pb2_grpc.InformationServicer):

    def SendHour(self, request, context):
        return services_pb2.HourReply(hour = g_hour)

class Aplication:
    def __init__(self, master):
        self.master = master
        self.queue = queue.Queue()

        self.gui = servergui.GuiPart(master, self.queue)

        self.clock1 = None
        self.clock2 = None
        self.clock3 = None
        self.clock4 = None

        self.databaseConnection = utcdatabase.UTCDatabase(database_location)

        #Server configurations
        self.port = str(sys.argv[1])
        self.servers = (str(sys.argv[2])).split(',')

        self.thread1 = threading.Thread(target=self.workerThread, args=[1], daemon=True).start()
        self.thread2 = threading.Thread(target=self.workerThread, args=[2], daemon=True).start()
        self.thread3 = threading.Thread(target=self.workerThread, args=[3], daemon=True).start()
        self.thread4 = threading.Thread(target=self.workerThread, args=[4], daemon=True).start()

        self.thread6 = threading.Thread(target=self.serve).start()
        self.thread7 = threading.Thread(target=self.consume).start()

        self.periodicCall()

    def periodicCall(self):
        self.gui.processIncoming()
        self.master.after(100, self.periodicCall)

    def workerThread(self, n_thread):
        global g_hour, g_pause

        if n_thread == 1:
            current_time = timer.getCurrentTime()
        else:
            current_time = timer.getRandomTime()

        while True:
            time.sleep(1)
            btn_id, is_editeable_btn = self.gui.getEditable(n_thread)
            setattr(self, 'clock' + str(n_thread), current_time)

            if g_pause:
                time.sleep(2)

            if n_thread == 1 and g_hour:
                current_time = g_hour
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
        global g_hour, g_pause, g_data
        ips = set()

        while True:
            g_slaves_hour = []
            for server in self.servers:
                server_data = server.split(':')
                ip_server = str(server_data[0])
                port_server = str(server_data[1])

                #get all the slave hours
                try:
                    start = time.time()
                    c_response = conection.callService('GetHour',ip_server,port_server)
                    end = time.time()

                    #Insert the ip and latency into the database if it´s a new one
                    if ip_server not in ips:
                        latency = str(end - start)
                        self.databaseConnection.insertIntoSlaves(ip_server, latency)

                    g_data[ip_server] = c_response.hour

                    splitted_hour = c_response.hour.split(":")
                    splitted_g_hour = g_hour.split(":")
                    if abs(int(splitted_g_hour[0]) - int(splitted_hour[1])) >= 1:
                        pass
                    elif abs(int(splitted_g_hour[1]) - int(splitted_hour[1])) >= 30:
                        pass
                    else:
                        g_slaves_hour.append(timer.differenceBetween(g_hour,c_response.hour))
                    sys.stdout.flush()
                except Exception as ex:
                    print(ex)
                    sys.stdout.flush()
            pause, berkely_hour = timer.getBerkleyhour(g_hour, g_slaves_hour)
            self.databaseConnection.insertIntoHours(g_hour, berkely_hour)
            self.databaseConnection.insertIntoMaster(g_data)
            g_hour = berkely_hour
            #self.databaseConnection.selectAllHour()
            self.databaseConnection.selectAllMaster()
            time.sleep(4)

    def getClock(self, number):
        return getattr(self, 'clock' + str(number))

root = tkinter.Tk()
client = Aplication(root)
root.mainloop()