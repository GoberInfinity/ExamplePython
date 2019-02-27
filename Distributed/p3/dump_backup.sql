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
                            book_id integer);
INSERT INTO "detail" VALUES(1,1,4);
INSERT INTO "detail" VALUES(2,1,2);
INSERT INTO "detail" VALUES(3,1,5);
INSERT INTO "detail" VALUES(4,1,4);
INSERT INTO "detail" VALUES(5,1,2);
INSERT INTO "detail" VALUES(6,1,5);
INSERT INTO "detail" VALUES(7,1,7);
INSERT INTO "detail" VALUES(8,1,6);
INSERT INTO "detail" VALUES(9,1,1);
INSERT INTO "detail" VALUES(10,1,5);
INSERT INTO "detail" VALUES(11,1,1);
INSERT INTO "detail" VALUES(12,1,4);
INSERT INTO "detail" VALUES(13,1,7);
INSERT INTO "detail" VALUES(14,1,3);
INSERT INTO "detail" VALUES(15,1,6);
CREATE TABLE session
                           (session_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id integer,
                            created DATETIME);
INSERT INTO "session" VALUES(1,1,'2019-02-27 00:36:04.999681');
INSERT INTO "session" VALUES(2,1,'2019-02-27 00:36:17.915330');
INSERT INTO "session" VALUES(3,1,'2019-02-27 00:40:22.644910');
INSERT INTO "session" VALUES(4,1,'2019-02-27 00:43:06.759541');
INSERT INTO "session" VALUES(5,1,'2019-02-27 00:45:15.542065');
INSERT INTO "session" VALUES(6,1,'2019-02-27 00:45:49.355688');
INSERT INTO "session" VALUES(7,1,'2019-02-27 00:47:50.967534');
INSERT INTO "session" VALUES(8,1,'2019-02-27 00:49:15.691491');
INSERT INTO "session" VALUES(9,1,'2019-02-27 00:51:28.230090');
INSERT INTO "session" VALUES(10,1,'2019-02-27 00:55:09.730078');
INSERT INTO "session" VALUES(11,1,'2019-02-27 00:55:23.566539');
INSERT INTO "session" VALUES(12,1,'2019-02-27 00:55:55.785649');
INSERT INTO "session" VALUES(13,1,'2019-02-27 00:58:54.166455');
INSERT INTO "session" VALUES(14,1,'2019-02-27 00:59:01.426750');
INSERT INTO "session" VALUES(15,1,'2019-02-27 00:59:12.418659');
INSERT INTO "session" VALUES(16,1,'2019-02-27 01:13:35.921454');
INSERT INTO "session" VALUES(17,1,'2019-02-27 01:13:40.294374');
INSERT INTO "session" VALUES(18,1,'2019-02-27 01:13:46.440082');
INSERT INTO "session" VALUES(19,1,'2019-02-27 01:15:44.486839');
INSERT INTO "session" VALUES(20,1,'2019-02-27 01:16:17.456395');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('book',7);
INSERT INTO "sqlite_sequence" VALUES('user',20);
INSERT INTO "sqlite_sequence" VALUES('session',20);
INSERT INTO "sqlite_sequence" VALUES('detail',15);
CREATE TABLE user
                           (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ip text UNIQUE);
INSERT INTO "user" VALUES(1,'127.0.0.1');
COMMIT;
