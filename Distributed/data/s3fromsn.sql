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
INSERT INTO "detail" VALUES(28,1,1);
INSERT INTO "detail" VALUES(29,1,2);
INSERT INTO "detail" VALUES(30,1,6);
INSERT INTO "detail" VALUES(31,1,7);
INSERT INTO "detail" VALUES(32,1,5);
INSERT INTO "detail" VALUES(33,1,4);
INSERT INTO "detail" VALUES(34,1,6);
INSERT INTO "detail" VALUES(35,1,4);
INSERT INTO "detail" VALUES(36,1,5);
INSERT INTO "detail" VALUES(37,1,1);
INSERT INTO "detail" VALUES(38,1,3);
INSERT INTO "detail" VALUES(39,1,5);
INSERT INTO "detail" VALUES(40,1,4);
INSERT INTO "detail" VALUES(41,1,6);
INSERT INTO "detail" VALUES(42,1,1);
INSERT INTO "detail" VALUES(43,1,7);
INSERT INTO "detail" VALUES(44,1,3);
INSERT INTO "detail" VALUES(45,1,2);
INSERT INTO "detail" VALUES(46,1,4);
INSERT INTO "detail" VALUES(47,1,1);
INSERT INTO "detail" VALUES(48,1,5);
INSERT INTO "detail" VALUES(49,1,6);
INSERT INTO "detail" VALUES(50,1,6);
INSERT INTO "detail" VALUES(51,1,1);
INSERT INTO "detail" VALUES(52,1,5);
INSERT INTO "detail" VALUES(53,1,1);
INSERT INTO "detail" VALUES(54,1,6);
INSERT INTO "detail" VALUES(55,1,1);
INSERT INTO "detail" VALUES(56,1,3);
INSERT INTO "detail" VALUES(57,1,5);
INSERT INTO "detail" VALUES(58,1,6);
INSERT INTO "detail" VALUES(59,1,2);
INSERT INTO "detail" VALUES(60,1,7);
INSERT INTO "detail" VALUES(61,1,4);
INSERT INTO "detail" VALUES(62,1,4);
INSERT INTO "detail" VALUES(63,1,5);
INSERT INTO "detail" VALUES(64,1,7);
INSERT INTO "detail" VALUES(65,1,1);
INSERT INTO "detail" VALUES(66,1,3);
INSERT INTO "detail" VALUES(67,1,4);
INSERT INTO "detail" VALUES(68,1,2);
INSERT INTO "detail" VALUES(69,1,6);
INSERT INTO "detail" VALUES(70,1,4);
INSERT INTO "detail" VALUES(71,1,1);
INSERT INTO "detail" VALUES(72,1,7);
INSERT INTO "detail" VALUES(73,1,2);
INSERT INTO "detail" VALUES(74,1,6);
INSERT INTO "detail" VALUES(75,1,3);
INSERT INTO "detail" VALUES(76,1,4);
INSERT INTO "detail" VALUES(77,1,5);
INSERT INTO "detail" VALUES(78,1,6);
INSERT INTO "detail" VALUES(79,1,4);
INSERT INTO "detail" VALUES(80,1,2);
INSERT INTO "detail" VALUES(81,1,3);
INSERT INTO "detail" VALUES(82,1,5);
INSERT INTO "detail" VALUES(83,1,1);
INSERT INTO "detail" VALUES(84,1,7);
INSERT INTO "detail" VALUES(85,1,7);
INSERT INTO "detail" VALUES(86,1,2);
INSERT INTO "detail" VALUES(87,1,4);
INSERT INTO "detail" VALUES(88,1,3);
INSERT INTO "detail" VALUES(89,1,6);
INSERT INTO "detail" VALUES(90,1,7);
INSERT INTO "detail" VALUES(91,1,5);
INSERT INTO "detail" VALUES(92,1,1);
INSERT INTO "detail" VALUES(93,1,5);
INSERT INTO "detail" VALUES(94,1,7);
INSERT INTO "detail" VALUES(95,1,2);
INSERT INTO "detail" VALUES(96,1,5);
INSERT INTO "detail" VALUES(97,1,6);
INSERT INTO "detail" VALUES(98,1,4);
INSERT INTO "detail" VALUES(99,1,7);
INSERT INTO "detail" VALUES(100,1,3);
INSERT INTO "detail" VALUES(101,1,1);
INSERT INTO "detail" VALUES(102,1,3);
INSERT INTO "detail" VALUES(103,1,2);
INSERT INTO "detail" VALUES(104,1,5);
INSERT INTO "detail" VALUES(105,1,7);
INSERT INTO "detail" VALUES(106,1,6);
INSERT INTO "detail" VALUES(107,1,4);
INSERT INTO "detail" VALUES(108,1,1);
INSERT INTO "detail" VALUES(109,1,7);
INSERT INTO "detail" VALUES(110,1,1);
INSERT INTO "detail" VALUES(111,1,3);
INSERT INTO "detail" VALUES(112,1,2);
INSERT INTO "detail" VALUES(113,1,6);
INSERT INTO "detail" VALUES(114,1,5);
INSERT INTO "detail" VALUES(115,1,4);
INSERT INTO "detail" VALUES(116,1,6);
INSERT INTO "detail" VALUES(117,1,5);
INSERT INTO "detail" VALUES(118,1,1);
INSERT INTO "detail" VALUES(119,1,3);
INSERT INTO "detail" VALUES(120,1,2);
INSERT INTO "detail" VALUES(121,1,4);
INSERT INTO "detail" VALUES(122,1,7);
INSERT INTO "detail" VALUES(123,1,5);
INSERT INTO "detail" VALUES(124,1,3);
INSERT INTO "detail" VALUES(125,1,6);
INSERT INTO "detail" VALUES(126,1,2);
INSERT INTO "detail" VALUES(127,1,1);
INSERT INTO "detail" VALUES(128,1,4);
INSERT INTO "detail" VALUES(129,1,1);
INSERT INTO "detail" VALUES(130,1,5);
INSERT INTO "detail" VALUES(131,1,4);
INSERT INTO "detail" VALUES(132,1,3);
INSERT INTO "detail" VALUES(133,1,2);
INSERT INTO "detail" VALUES(134,1,7);
INSERT INTO "detail" VALUES(135,1,6);
INSERT INTO "detail" VALUES(136,1,7);
INSERT INTO "detail" VALUES(137,68,7);
INSERT INTO "detail" VALUES(138,68,5);
INSERT INTO "detail" VALUES(139,NULL,2);
INSERT INTO "detail" VALUES(140,68,1);
INSERT INTO "detail" VALUES(141,NULL,3);
INSERT INTO "detail" VALUES(142,68,4);
INSERT INTO "detail" VALUES(143,NULL,7);
INSERT INTO "detail" VALUES(144,70,1);
INSERT INTO "detail" VALUES(145,68,5);
INSERT INTO "detail" VALUES(146,70,6);
INSERT INTO "detail" VALUES(147,1,7);
INSERT INTO "detail" VALUES(148,1,4);
INSERT INTO "detail" VALUES(149,1,3);
INSERT INTO "detail" VALUES(150,1,2);
INSERT INTO "detail" VALUES(151,1,7);
INSERT INTO "detail" VALUES(152,1,6);
INSERT INTO "detail" VALUES(153,1,5);
INSERT INTO "detail" VALUES(154,1,2);
INSERT INTO "detail" VALUES(155,1,4);
INSERT INTO "detail" VALUES(156,1,3);
INSERT INTO "detail" VALUES(157,1,1);
INSERT INTO "detail" VALUES(158,1,2);
INSERT INTO "detail" VALUES(159,1,1);
INSERT INTO "detail" VALUES(160,1,7);
INSERT INTO "detail" VALUES(161,1,4);
INSERT INTO "detail" VALUES(162,1,6);
INSERT INTO "detail" VALUES(163,1,4);
INSERT INTO "detail" VALUES(164,1,5);
INSERT INTO "detail" VALUES(165,1,1);
INSERT INTO "detail" VALUES(166,1,2);
INSERT INTO "detail" VALUES(167,1,3);
INSERT INTO "detail" VALUES(168,1,7);
INSERT INTO "detail" VALUES(169,1,6);
INSERT INTO "detail" VALUES(170,1,6);
INSERT INTO "detail" VALUES(171,1,1);
INSERT INTO "detail" VALUES(172,1,4);
INSERT INTO "detail" VALUES(173,1,3);
INSERT INTO "detail" VALUES(174,1,1);
INSERT INTO "detail" VALUES(175,1,7);
INSERT INTO "detail" VALUES(176,1,3);
INSERT INTO "detail" VALUES(177,1,5);
INSERT INTO "detail" VALUES(178,1,2);
INSERT INTO "detail" VALUES(179,1,6);
INSERT INTO "detail" VALUES(180,1,4);
INSERT INTO "detail" VALUES(181,1,1);
INSERT INTO "detail" VALUES(182,1,2);
INSERT INTO "detail" VALUES(183,1,3);
INSERT INTO "detail" VALUES(184,1,4);
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
INSERT INTO "session" VALUES(42,1,'2019-03-18 03:09:07.769580');
INSERT INTO "session" VALUES(43,1,'2019-03-18 03:09:11.975605');
INSERT INTO "session" VALUES(44,1,'2019-03-18 03:09:13.848994');
INSERT INTO "session" VALUES(45,1,'2019-03-29 03:09:43.452993');
INSERT INTO "session" VALUES(46,1,'2019-03-29 03:11:17.161739');
INSERT INTO "session" VALUES(47,1,'2019-03-29 03:23:09.456738');
INSERT INTO "session" VALUES(48,1,'2019-03-29 03:38:01.087806');
INSERT INTO "session" VALUES(49,1,'2019-03-29 03:45:45.199411');
INSERT INTO "session" VALUES(50,1,'2019-03-29 03:46:22.562665');
INSERT INTO "session" VALUES(51,1,'2019-03-29 03:55:20.636089');
INSERT INTO "session" VALUES(52,1,'2019-03-29 03:56:03.054595');
INSERT INTO "session" VALUES(53,1,'2019-03-29 03:57:10.751363');
INSERT INTO "session" VALUES(54,1,'2019-03-29 03:59:54.063896');
INSERT INTO "session" VALUES(55,1,'2019-03-29 04:00:16.610480');
INSERT INTO "session" VALUES(56,1,'2019-03-29 04:14:45.926456');
INSERT INTO "session" VALUES(57,1,'2019-03-29 04:15:09.076190');
INSERT INTO "session" VALUES(58,1,'2019-03-29 04:16:59.438524');
INSERT INTO "session" VALUES(59,1,'2019-03-29 04:17:03.949642');
INSERT INTO "session" VALUES(60,1,'2019-03-29 06:03:38.275772');
INSERT INTO "session" VALUES(61,1,'2019-03-29 06:03:47.110960');
INSERT INTO "session" VALUES(62,1,'2019-03-29 06:12:11.912089');
INSERT INTO "session" VALUES(63,1,'2019-03-29 06:12:22.574730');
INSERT INTO "session" VALUES(64,1,'2019-03-29 06:15:31.913625');
INSERT INTO "session" VALUES(65,1,'2019-03-29 06:22:49.989128');
INSERT INTO "session" VALUES(66,1,'2019-03-29 06:23:51.405340');
INSERT INTO "session" VALUES(67,1,'2019-03-29 06:24:36.136419');
INSERT INTO "session" VALUES(68,68,'2019-03-29 07:08:59.163304');
INSERT INTO "session" VALUES(69,68,'2019-03-29 07:13:55.766645');
INSERT INTO "session" VALUES(70,70,'2019-03-29 07:17:53.907794');
INSERT INTO "session" VALUES(71,68,'2019-03-29 07:18:04.164064');
INSERT INTO "session" VALUES(72,1,'2019-03-29 07:19:52.655096');
INSERT INTO "session" VALUES(73,1,'2019-03-29 07:21:23.115671');
INSERT INTO "session" VALUES(74,1,'2019-03-29 07:24:18.366814');
INSERT INTO "session" VALUES(75,1,'2019-03-29 07:40:09.111957');
INSERT INTO "session" VALUES(76,1,'2019-03-29 07:40:16.767599');
INSERT INTO "session" VALUES(77,1,'2019-03-29 07:40:28.858514');
INSERT INTO "session" VALUES(78,1,'2019-03-29 07:42:04.779587');
INSERT INTO "session" VALUES(79,1,'2019-03-29 07:48:13.962634');
INSERT INTO "session" VALUES(80,1,'2019-03-29 07:48:20.190866');
INSERT INTO "session" VALUES(81,1,'2019-03-29 07:48:24.519284');
INSERT INTO "session" VALUES(82,1,'2019-03-29 07:50:17.310473');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('book',7);
INSERT INTO "sqlite_sequence" VALUES('user',82);
INSERT INTO "sqlite_sequence" VALUES('session',82);
INSERT INTO "sqlite_sequence" VALUES('detail',184);
CREATE TABLE user
                           (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            ip text UNIQUE);
INSERT INTO "user" VALUES(1,'127.0.0.1');
INSERT INTO "user" VALUES(68,'192.168.1.70:50060');
INSERT INTO "user" VALUES(70,'192.168.1.70:50070');
COMMIT;
