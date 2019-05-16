# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
#TODO
# Detaill, session tables changed, now it has to recieve time as parameter to insert into the database
class Database:

    def __init__(self, database_file):
        self.createConnection(database_file)
        """ Uncomment if you want to create a new empty database """
        #self.__createTables()
        #self.__insertBooks()
        #self.selectAllBooks()

    def closeDatabase(self):
        self.connection = None

    def createConnection(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)

    def __insertBooks(self):
        cursor = self.createCursor()
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('Viaje al centro de la tierra','Julio Verne','Porrua',100.00,'1.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('50 Sombras de Gray','E L James','Vintage',200.00,'2.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('1984','George Orwell','Debolsillo',300.00,'3.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('IT','Stephen King','Debolsillo',400.00,'4.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('La Perla','John Steinbeck','Esfinge',500.00,'5.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('Introduction to algorithms','Tomas Cormen','Limusa',600.00,'6.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('Cracking the coding interview','Gayle Mcdowell','Laakman',700.00,'7.png')")
        self.connection.commit()

    def selectAllBooks(self):
        cursor = self.createCursor()
        response = []
        for row in cursor.execute('SELECT * FROM book'):
            response.append(','.join(map(str, row)))
        return response

    def __createTables(self):
        cursor = self.createCursor()
        cursor.execute('''CREATE TABLE book
                           (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name text,
                            author text,
                            editorial text,
                            price real,
                            image text)''')
        cursor.execute('''CREATE TABLE user
                           (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ip text UNIQUE)''')
        cursor.execute('''CREATE TABLE session
                           (session_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id integer,
                            created text)
                            ''')
        cursor.execute('''CREATE TABLE detail
                           (detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            session integer,
                            book_id integer,
                            created text)
                            ''')

    def insertIntoUser(self, ip, time):
        cursor = self.createCursor()
        cursor.execute('INSERT OR IGNORE INTO user (ip) VALUES (?)', [ip])
        user_id = self.getIdUser(ip)
        cursor.execute('INSERT INTO session (user_id, created) VALUES (?,?)', [user_id, time])
        self.connection.commit()
        self.getAllUsers()
        self.getAllSessions()

    def getAllUsers(self):
        print("--USER TABLE--")
        cursor = self.createCursor()
        for row in cursor.execute('SELECT * FROM user'):
            print(row)

    def getIdUser(self, ip):
        cursor = self.createCursor()
        for row in cursor.execute('SELECT * FROM user'):
            if ip == row[1]:
                return row[0]

    def getAllSessions(self):
        print("--SESSION TABLE--")
        cursor = self.createCursor()
        for row in cursor.execute('SELECT * FROM session'):
            print(row)

    def getAllDetaill(self):
        print("--DETAILL TABLE--")
        cursor = self.createCursor()
        for row in cursor.execute('SELECT * FROM detail'):
            print(row)

    def exportDatabase(self, path_to_export):
        with open(path_to_export, 'w') as f:
            for line in self.connection.iterdump():
                f.write('%s\n' % line)

    def getSession(self, ip):
        cursor = self.createCursor()
        user_id = self.getIdUser(ip)
        for row in cursor.execute('SELECT * FROM session'):
            if user_id == row[1]:
                return row[0]

    def insertDetail(self, ip, book_id, time):
        cursor = self.createCursor()
        session_id = self.getSession(ip)
        cursor.execute('INSERT INTO detail (session, book_id, created) VALUES (?,?,?)', [session_id, book_id, time])
        self.connection.commit()
        self.getAllDetaill()

    def createCursor(self):
        return self.connection.cursor()

    def closeConnection(self):
        self.connection.close()

#a = Database("recovery.db")