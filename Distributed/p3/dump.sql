BEGIN TRANSACTION;
CREATE TABLE book
                           (book_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            name text, 
                            author text, 
                            editorial text, 
                            price real, 
                            image text);
INSERT INTO "book" VALUES(1,'Uno','Pepe','EdPepe',100.0,'1.png');
INSERT INTO "book" VALUES(2,'Dos','Pepe','EdPepe',200.0,'2.png');
INSERT INTO "book" VALUES(3,'Tres','Pepe','EdPepe',300.0,'3.png');
INSERT INTO "book" VALUES(4,'Cuatro','Pepe','EdPepe',400.0,'4.png');
INSERT INTO "book" VALUES(5,'Cinco','Pepe','EdPepe',500.0,'5.png');
INSERT INTO "book" VALUES(6,'Seis','Pepe','EdPepe',600.0,'6.png');
INSERT INTO "book" VALUES(7,'Siete','Pepe','EdPepe',700.0,'7.png');
CREATE TABLE detail
                           (detail_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            session integer,
                            book_id integer);
INSERT INTO "detail" VALUES(1,3,5);
INSERT INTO "detail" VALUES(2,3,4);
INSERT INTO "detail" VALUES(3,3,6);
INSERT INTO "detail" VALUES(4,3,1);
INSERT INTO "detail" VALUES(5,3,3);
INSERT INTO "detail" VALUES(6,3,2);
INSERT INTO "detail" VALUES(7,3,4);
INSERT INTO "detail" VALUES(8,3,7);
INSERT INTO "detail" VALUES(9,3,2);
INSERT INTO "detail" VALUES(10,3,6);
INSERT INTO "detail" VALUES(11,3,1);
INSERT INTO "detail" VALUES(12,3,3);
INSERT INTO "detail" VALUES(13,3,7);
INSERT INTO "detail" VALUES(14,3,4);
INSERT INTO "detail" VALUES(15,3,6);
INSERT INTO "detail" VALUES(16,3,1);
INSERT INTO "detail" VALUES(17,3,3);
INSERT INTO "detail" VALUES(18,3,5);
INSERT INTO "detail" VALUES(19,3,2);
INSERT INTO "detail" VALUES(20,3,5);
CREATE TABLE session
                           (session_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            user_id integer,
                            created DATETIME,
                            exited DATETIME);
INSERT INTO "session" VALUES(1,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(2,NULL,'2019-02-24',NULL);
INSERT INTO "session" VALUES(3,6,'2019-02-24',NULL);
INSERT INTO "session" VALUES(4,6,'2019-02-24',NULL);
INSERT INTO "session" VALUES(5,6,'2019-02-24',NULL);
INSERT INTO "session" VALUES(6,6,'2019-02-24',NULL);
INSERT INTO "session" VALUES(7,6,'2019-02-24',NULL);
INSERT INTO "session" VALUES(8,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(9,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(10,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(11,6,'2019-02-24',NULL);
INSERT INTO "session" VALUES(12,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(13,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(14,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(15,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(16,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(17,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(18,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(19,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(20,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(21,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(22,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(23,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(24,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(25,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(26,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(27,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(28,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(29,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(30,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(31,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(32,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(33,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(34,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(35,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(36,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(37,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(38,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(39,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(40,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(41,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(42,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(43,3,'2019-02-24',NULL);
INSERT INTO "session" VALUES(44,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(45,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(46,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(47,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(48,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(49,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(50,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(51,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(52,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(53,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(54,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(55,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(56,6,'2019-02-25',NULL);
INSERT INTO "session" VALUES(57,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(58,6,'2019-02-25',NULL);
INSERT INTO "session" VALUES(59,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(60,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(61,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(62,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(63,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(64,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(65,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(66,6,'2019-02-25',NULL);
INSERT INTO "session" VALUES(67,3,'2019-02-25',NULL);
INSERT INTO "session" VALUES(68,6,'2019-02-25',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('book',7);
INSERT INTO "sqlite_sequence" VALUES('user',72);
INSERT INTO "sqlite_sequence" VALUES('session',68);
INSERT INTO "sqlite_sequence" VALUES('detail',20);
CREATE TABLE user
                           (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            ip text UNIQUE);
INSERT INTO "user" VALUES(1,'(''127.0.0.1'', 61195)');
INSERT INTO "user" VALUES(2,'(''127.0.0.1'', 63429)');
INSERT INTO "user" VALUES(3,'127.0.0.1');
INSERT INTO "user" VALUES(6,'192.168.1.74');
COMMIT;
