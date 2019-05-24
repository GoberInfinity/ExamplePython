# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime

database_file = 'data/utcdb/u_db.db'

class UTCDatabase:

    def __init__(self):
        self.createConnection(database_file)
        self.selectAllSlave()
        self.selectAllHour()
        self.selectAllMaster()

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

    def insertIntoMaster(self, data):
        if not data:
            return
        last_hour_id = self.getLastInsertedHour()
        for ip, hour in data.items():
            slave_id = int(self.getIdOfSlave(ip))
            cursor = self.createCursor()
            cursor.execute('INSERT OR IGNORE INTO master (slave_id, hour_id, slave_hour) VALUES (?,?,?)', [slave_id, last_hour_id, hour])
            self.connection.commit()

    def getIdOfSlave(self, ip):
        cursor = self.createCursor()
        for row in cursor.execute('SELECT * FROM slave'):
            if ip == row[1]:
                return row[0]

    def getLastInsertedHour(self):
        cursor = self.createCursor()
        cursor.execute('SELECT * FROM hour ORDER BY hour_id DESC LIMIT 1')
        return int(cursor.fetchone()[0])

    def createCursor(self):
        return self.connection.cursor()

    def closeConnection(self):
        self.connection.close()

    def selectAllMaster(self):
        cursor = self.createCursor()
        response = []
        print("MASTER TABLE")
        for row in cursor.execute('SELECT * FROM master '):
            print(row)

    def selectAllHour(self):
        cursor = self.createCursor()
        response = []
        print("HOUR TABLE")
        for row in cursor.execute('SELECT * FROM hour '):
            print(row)
    
    def selectAllSlave(self):
        cursor = self.createCursor()
        response = []
        print("SLAVE TABLE")
        for row in cursor.execute('SELECT * FROM slave '):
            print(row)

a = UTCDatabase()