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
INSERT INTO "detail" VALUES(16,1,1);
INSERT INTO "detail" VALUES(17,1,2);
INSERT INTO "detail" VALUES(18,1,3);
INSERT INTO "detail" VALUES(19,1,7);
INSERT INTO "detail" VALUES(20,1,4);
INSERT INTO "detail" VALUES(21,1,5);
INSERT INTO "detail" VALUES(22,1,5);
INSERT INTO "detail" VALUES(23,1,3);
INSERT INTO "detail" VALUES(24,1,4);
INSERT INTO "detail" VALUES(25,1,5);
INSERT INTO "detail" VALUES(26,1,7);
INSERT INTO "detail" VALUES(27,1,4);
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
INSERT INTO "session" VALUES(21,1,'2019-03-18 00:17:49.705230');
INSERT INTO "session" VALUES(22,1,'2019-03-18 00:22:31.807499');
INSERT INTO "session" VALUES(23,1,'2019-03-18 00:26:58.941837');
INSERT INTO "session" VALUES(24,1,'2019-03-18 00:37:51.874442');
INSERT INTO "session" VALUES(25,1,'2019-03-18 00:38:18.701004');
INSERT INTO "session" VALUES(26,1,'2019-03-18 00:51:32.006040');
INSERT INTO "session" VALUES(27,1,'2019-03-18 00:51:39.078770');
INSERT INTO "session" VALUES(28,1,'2019-03-18 00:53:36.148001');
INSERT INTO "session" VALUES(29,1,'2019-03-18 00:53:38.221508');
INSERT INTO "session" VALUES(30,1,'2019-03-18 00:57:50.080365');
INSERT INTO "session" VALUES(31,1,'2019-03-18 00:57:55.489688');
INSERT INTO "session" VALUES(32,1,'2019-03-18 01:06:20.305285');
INSERT INTO "session" VALUES(33,1,'2019-03-18 01:06:27.289993');
INSERT INTO "session" VALUES(34,1,'2019-03-18 01:23:50.873624');
INSERT INTO "session" VALUES(35,1,'2019-03-18 01:23:53.364233');
INSERT INTO "session" VALUES(36,1,'2019-03-18 01:25:03.316342');
INSERT INTO "session" VALUES(37,1,'2019-03-18 01:25:10.308052');
INSERT INTO "session" VALUES(38,1,'2019-03-18 01:27:51.905991');
INSERT INTO "session" VALUES(39,1,'2019-03-18 01:27:54.142538');
INSERT INTO "session" VALUES(40,1,'2019-03-18 01:29:23.247595');
INSERT INTO "session" VALUES(41,1,'2019-03-18 01:29:26.012270');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('book',7);
INSERT INTO "sqlite_sequence" VALUES('user',41);
INSERT INTO "sqlite_sequence" VALUES('session',41);
INSERT INTO "sqlite_sequence" VALUES('detail',27);
CREATE TABLE user
                           (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ip text UNIQUE);
INSERT INTO "user" VALUES(1,'127.0.0.1');
COMMIT;
