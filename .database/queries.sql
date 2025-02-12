-- CREATE TABLE Reviews (id INTEGER PRIMARY KEY AUTOINCREMENT,
--                       user_id INTEGER,
--                       date TEXT NOT NULL,
--                       rating INTEGER,
--                       title TEXT NOT NULL,
--                       review TEXT NOT NULL);

-- CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT,
--                     username TEXT NOT NULL,
--                     password TEXT NOT NULL);

-- INSERT INTO Users(username, password)
--             VALUES("johnno", "scrypt:32768:8:1$ZIUB1D5lCNl2GZ5w$4de3cadd75e3f03617e0c7423a3aab85a84fd9dea009295ce41d438e52da3cbc0b64def6ecbaaef13255c4918585c15e6c313d8d98d64f37c37d22b3e25bf04e");

-- INSERT INTO Users(username, password)
--             VALUES("lachlan", "scrypt:32768:8:1$YfnN0EtmRGYdDphU$6803d35904ca054bc23232df87abd76ec9fe75eae8fe21301146f8bcfc1649715a787e218cb2a7463ab1d11b4e0186cf0541144aaf554d022cd9fc9395b2cae8"),
--                   ("jilian", "scrypt:32768:8:1$LaSx68XLEuZ1TWJU$0aa3b35c461bcf8343554773d6a3957b7b22af7a902403b5f7e1574d42b4e7630959b483af7a5d22e3bc1659ccd6eb1209917c8537417fddc1e6960bb43a4b04"),
--                   ("rose", "scrypt:32768:8:1$FdOgvhXqmAAY5465$192fa886bc701dd88b4b73be9ee356af23c83fc9918fcfa8cb40cbc65ff3c31f0d99ac02fd12f6c2b218ef8a518055b1391ef02a5456daa277711d7ee5c02a05"),
--                   ("bjorn", "scrypt:32768:8:1$19yCXh84aS6I31Z3$9cf8bf32640359830b8bac6a8f8ea46ca4c6f78dbc607769ea887c9415bd7c8754dad12cdc41c9570fa849b3a26a0d55aedaca2f770ac7ea74342f5728686109");

-- INSERT INTO Guesses(user_id, date, score, game)
--             VALUES(1, "2024-10-27", 3, "Brute Force"),
--                   (1, "2024-10-28", 2, "Star Wars: Knights of the Old Republic II"),
--                   (2, "2024-10-29", 6, "Zenless Zone Zero"),
--                   (2, "2024-10-30", 0, "Earthworm Jim"),
--                   (3, "2024-10-31", 1, "Yoshi's Island DS"),
--                   (3, "2024-11-01", 3, "The Witcher"),
--                   (4, "2024-11-02", 5, "Abe's Odyssey"),
--                   (4, "2024-11-03", 3, "SCP: Secret Laboratory"),
--                   (5, "2024-11-04", 3, "Resident Evil 3"),
--                   (5, "2024-11-05", 2, "Dead Space 3");

-- INSERT INTO Reviews(user_id, date, rating, title, review)
--             VALUES(1, "2024-10-27", 3, "Encanto", "Good but not great"),
--                   (1, "2024-10-28", 4, "Nosferatu", "Scary"),
--                   (2, "2024-10-29", 5, "The Dark Knight", "Peak"),
--                   (2, "2024-10-30", 0, "Pacific Rim Uprising", "This shouldn't exist"),
--                   (3, "2024-10-31", 5, "Knives Out", "Shocking"), 
--                   (3, "2024-11-01", 5, "Oppenheimer", "Cinematic masterpiece"),
--                   (4, "2024-11-02", 2, "Wish", "meh"),
--                   (4, "2024-11-03", 3, "The Amazing Spiderman 2", "Green Gooblin"),
--                   (5, "2024-11-04", 5, "Spiderman 2", "Peak superheroism"),
--                   (5, "2024-11-05", 4, "Spiderman 3", "Good Movie");

-- DELETE FROM Users WHERE id = 8;