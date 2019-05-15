# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime

class UTCDatabase:

    def __init__(self, database_file):
        self.createConnection(database_file)
        try:
            self.__createTables()
        except:
            print("Already created")

    def createConnection(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)

    def __createTables(self):
        cursor = self.createCursor()
        cursor.execute('''CREATE TABLE slave
                           (slave_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ip text UNIQUE,
                            latency real)''')
        cursor.execute('''CREATE TABLE hour
                           (hour_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            p_hour text,
                            c_hour text)''')
        cursor.execute('''CREATE TABLE master
                           (master_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            slave_id integer,
                            hour_id integer,
                            slave_hour text)
                            ''')

    def insertIntoSlaves(self, ip, latency):
        cursor = self.createCursor()
        cursor.execute('INSERT OR IGNORE INTO slave (ip, latency) VALUES (?,?)', [ip, latency])
        self.connection.commit()

    def insertIntoHours(self, master, berkley):
        cursor = self.createCursor()
        cursor.execute('INSERT OR IGNORE INTO hour (p_hour, c_hour) VALUES (?,?)', [master, berkley])
        self.connection.commit()

    def insertIntoMaster(self, slave_id, master_id, slave_hour):
        cursor = self.createCursor()
        cursor.execute('INSERT OR IGNORE INTO master (slave_id, hour_id_hour, slave_hour) VALUES (?,?)', [slave_id, master_id, slave_hour])
        self.connection.commit()

    def createCursor(self):
        return self.connection.cursor()

    def closeConnection(self):
        self.connection.close()

    def selectAllHour(self):
        cursor = self.createCursor()
        response = []
        for row in cursor.execute('SELECT * FROM hour'):
            print(row, end=" ")