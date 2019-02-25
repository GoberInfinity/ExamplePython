# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime

database_file = 'database.db'

class Database:
     
    connection = None
    
    def __init__(self):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        #self.__createTables()
        #self.__insertBooks()
        #self.selectAllBooks()

    def __insertBooks(self):
        cursor = self.createCursor()
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('Uno','Pepe','EdPepe',100.00,'1.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('Dos','Pepe','EdPepe',200.00,'2.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('Tres','Pepe','EdPepe',300.00,'3.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('Cuatro','Pepe','EdPepe',400.00,'4.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('Cinco','Pepe','EdPepe',500.00,'5.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('Seis','Pepe','EdPepe',600.00,'6.png')")
        cursor.execute("INSERT INTO book (name, author, editorial, price, image) VALUES ('Siete','Pepe','EdPepe',700.00,'7.png')")
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
                            created DATETIME,
                            exited DATETIME)
                            ''')
        cursor.execute('''CREATE TABLE detail
                           (detail_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            session integer,
                            book_id integer)
                            ''')
                            
    def insertIntoUser(self, ip):
        cursor = self.createCursor()
        time=datetime.now()
        user_id = self.getIdUser(ip)
        cursor.execute('INSERT OR IGNORE INTO user (ip) VALUES (?)', [ip])
        cursor.execute('INSERT INTO session (user_id, created) VALUES (?,?)', [user_id, time.strftime('%Y-%m-%d')])
        self.connection.commit()
        self.getAllUsers()
        self.getAllSessions()
        
    def getAllUsers(self):
        cursor = self.createCursor()
        for row in cursor.execute('SELECT * FROM user'):
            print(row)
            
    def getIdUser(self, ip):
        cursor = self.createCursor()
        for row in cursor.execute('SELECT * FROM user'):
            if ip == row[1]:
                return row[0]
            
    def getAllSessions(self):
        cursor = self.createCursor()
        for row in cursor.execute('SELECT * FROM session'):
            print(row)
            
    def getAllDetaill(self):
        cursor = self.createCursor()
        for row in cursor.execute('SELECT * FROM detail'):
            print(row)
            
    def getSession(self, ip):
        cursor = self.createCursor()
        user_id = self.getIdUser()
        for row in cursor.execute('SELECT * FROM user'):
            if user_id == row[1]:
                return row[0]
            
    def insertDetail(self, ip, book_id):
        cursor = self.createCursor()
        session_id = self.getSession(ip)
        cursor.execute('INSERT INTO detail (session, book_id) VALUES (? ?)', [session_id, book_id])
        
                               
    def createCursor(self):
        return self.connection.cursor()
        
    def closeConnection(self):
        self.connection.close()