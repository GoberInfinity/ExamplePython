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
INSERT INTO "session" VALUES(21,1,'2019-03-07 23:56:11.699460');
INSERT INTO "session" VALUES(22,1,'2019-03-07 23:59:17.565803');
INSERT INTO "session" VALUES(23,1,'2019-03-07 23:59:19.693324');
INSERT INTO "session" VALUES(24,1,'2019-03-07 23:59:20.006400');
INSERT INTO "session" VALUES(25,1,'2019-03-07 23:59:23.123164');
INSERT INTO "session" VALUES(26,1,'2019-03-07 23:59:33.096605');
INSERT INTO "session" VALUES(27,1,'2019-03-07 23:59:39.638413');
INSERT INTO "session" VALUES(28,1,'2019-03-08 00:04:02.751640');
INSERT INTO "session" VALUES(29,1,'2019-03-08 00:07:19.581405');
INSERT INTO "session" VALUES(30,1,'2019-03-08 00:10:16.434039');
INSERT INTO "session" VALUES(31,1,'2019-03-08 00:11:21.310927');
INSERT INTO "session" VALUES(32,1,'2019-03-12 23:35:00.341925');
INSERT INTO "session" VALUES(33,1,'2019-03-12 23:35:18.508385');
INSERT INTO "session" VALUES(34,1,'2019-03-13 01:18:42.535168');
INSERT INTO "session" VALUES(35,1,'2019-03-13 01:21:31.826872');
INSERT INTO "session" VALUES(36,1,'2019-03-13 01:24:20.176027');
INSERT INTO "session" VALUES(37,1,'2019-03-13 01:26:16.787132');
INSERT INTO "session" VALUES(38,1,'2019-03-13 01:39:45.587992');
INSERT INTO "session" VALUES(39,1,'2019-03-13 01:41:07.304927');
INSERT INTO "session" VALUES(40,1,'2019-03-13 01:42:44.118065');
INSERT INTO "session" VALUES(41,1,'2019-03-13 02:01:42.005842');
INSERT INTO "session" VALUES(42,1,'2019-03-13 02:04:23.956975');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('book',7);
INSERT INTO "sqlite_sequence" VALUES('user',42);
INSERT INTO "sqlite_sequence" VALUES('session',42);
INSERT INTO "sqlite_sequence" VALUES('detail',15);
CREATE TABLE user
                           (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ip text UNIQUE);
INSERT INTO "user" VALUES(1,'127.0.0.1');
COMMIT;
