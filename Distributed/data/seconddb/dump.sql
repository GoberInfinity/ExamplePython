BEGIN TRANSACTION;
CREATE TABLE book
                           (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name text,
                            author text,
                            editorial text,
                            price real,
                            image text);
INSERT INTO "book" VALUES(1,'Viaje al centro de la tierra','Julio Verne','Porrua',100.0,'1.png');
INSERT INTO "book" VALUES(2,'50 Sombras de Gray','E L James','Vintage',200.0,'2.png');
INSERT INTO "book" VALUES(3,'1984','George Orwell','Debolsillo',300.0,'3.png');
INSERT INTO "book" VALUES(4,'IT','Stephen King','Debolsillo',400.0,'4.png');
INSERT INTO "book" VALUES(5,'La Perla','John Steinbeck','Esfinge',500.0,'5.png');
INSERT INTO "book" VALUES(6,'Introduction to algorithms','Tomas Cormen','Limusa',600.0,'6.png');
INSERT INTO "book" VALUES(7,'Cracking the coding interview','Gayle Mcdowell','Laakman',700.0,'7.png');
CREATE TABLE detail
                           (detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            session integer,
                            book_id integer,
                            created text);
INSERT INTO "detail" VALUES(1,1,4,'13:2:20');
INSERT INTO "detail" VALUES(2,1,2,'13:6:33');
INSERT INTO "detail" VALUES(3,1,3,'13:18:8');
INSERT INTO "detail" VALUES(4,1,7,'13:18:51');
INSERT INTO "detail" VALUES(5,1,1,'13:30:8');
CREATE TABLE session
                           (session_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id integer,
                            created text);
INSERT INTO "session" VALUES(1,1,'13:2:20');
INSERT INTO "session" VALUES(2,1,'13:6:33');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('book',7);
INSERT INTO "sqlite_sequence" VALUES('user',2);
INSERT INTO "sqlite_sequence" VALUES('session',2);
INSERT INTO "sqlite_sequence" VALUES('detail',5);
CREATE TABLE user
                           (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ip text UNIQUE);
INSERT INTO "user" VALUES(1,'127.0.0.1');
COMMIT;
