import sqlite3
from json import dumps



#conn = sqlite3.connect("db.db")
#cursor = conn.cursor()
#cursor.execute("""DELETE FROM USERS WHERE ID = 1""")
##cursor.execute("""CREATE TABLE USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT, LOGIN TEXT NOT NULL, PASSWORD TEXT NOT NULL, TYPE TEXT NOT NULL, BAN INTEGER NOT NULL);""")
#cursor.execute("""INSERT INTO USERS (LOGIN, PASSWORD, TYPE, BAN) VALUES ('admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'admin', 0);""")
##cursor.execute("""INSERT INTO USERS (LOGIN, PASSWORD, TYPE, BAN) VALUES ('John420', 'dc972f6d2917122b49a8aec765868a4b35d6a57cc3c09512110893edfaa49687', 'amateur', 0);""")
#conn.commit()
#conn.close()


# create USERS with admin admin admin and John420 John420! amateur
if 0:
	conn = sqlite3.connect("db.db")
	cursor = conn.cursor()
	cursor.execute("""CREATE TABLE USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT, LOGIN TEXT NOT NULL, EMAIL TEXT NOT NULL, PASSWORD TEXT NOT NULL, TYPE TEXT NOT NULL, BAN INTEGER NOT NULL);""")
	cursor.execute("""INSERT INTO USERS (LOGIN, EMAIL, PASSWORD, TYPE, BAN) VALUES ('admin', 'admin@admin.admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'admin', 0);""")
	cursor.execute("""INSERT INTO USERS (LOGIN, EMAIL, PASSWORD, TYPE, BAN) VALUES ('John420', 'john420@example.com', 'dc972f6d2917122b49a8aec765868a4b35d6a57cc3c09512110893edfaa49687', 'amateur', 0);""")
	conn.commit()
	conn.close()

# test unvrifiedpro to pro
if 0:
	conn = sqlite3.connect("db.db")
	cursor = conn.cursor()
	cursor.execute('''DELETE FROM USERS WHERE LOGIN = "test420";''')
	cursor.execute('''INSERT INTO USERS (LOGIN, PASSWORD, TYPE, BAN) VALUES ('test420', '1717486913556ff868b8b7606be2782feb971dd26d3d0e973c9664c5ded0f46c', 'proUnverified', 0);''')
	conn.commit()
	conn.close()

# create POSTS
if 0:
	conn = sqlite3.connect("db.db")
	cursor = conn.cursor()
	cursor.execute("""CREATE TABLE POSTS (ID INTEGER PRIMARY KEY AUTOINCREMENT,
	TITLE TEXT NOT NULL,
	CONTENT TEXT NOT NULL,
	DATE INTEGER NOT NULL,
	PUBLIC INTEGER NOT NULL,
	ATTACHMENTS BLOB NOT NULL,
	AUTHOR TEXT NOT NULL);""")
	conn.commit()
	conn.close()

if 0:
	conn = sqlite3.connect("db.db")
	cursor = conn.cursor()
	#cursor.execute("""INSERT INTO POSTS (TITLE, CONTENT, DATE, PUBLIC, ATTACHMENTS, AUTHOR) VALUES (?, ?, ?, ?, ?, ?)""", ("POST 1", "PUBLIC", 0, 1, dumps(["1.png"]), "JP2", ))
	#cursor.execute("""DELETE FROM POSTS WHERE ID = 1""")
	conn.commit()
	conn.close()

# create LICKS with one example
if 0:
	conn = sqlite3.connect("db.db")
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE LICKS (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
	TITLE TEXT NOT NULL, 
	CONTENT TEXT NOT NULL, 
	BRIEF TEXT NOT NULL, 
	DATE INTEGER NOT NULL, 
	ATTACHMENTS BLOB NOT NULL, 
	AUTHOR TXT NOT NULL, 
	BEAT TEXT NOT NULL, 
	TEMPO TEXT NOT NULL, 
	TYPE TEXT NOT NULL, 
	DIFFICULTY TEXT NOT NULL)''')
	#cursor.execute('''INSERT INTO LICKS (TITLE, CONTENT, DATE, ATTACHMENTS, AUTHOR, BEAT, TEMPO, TYPE, DIFFICULTY) VALUES ("test1", "content1", 0, ?, "admin", "2/3", "240bpm", "frenchcore", "hard");''', (dumps(["a.png", "b.mp4", "c.mp3"]),))
	conn.commit()
	conn.close()

# create LESSONS with one example
if 0:
	conn = sqlite3.connect("db.db")
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE LESSONS (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
		TITLE TEXT NOT NULL, 
		CONTENT TEXT NOT NULL, 
		BRIEF TEXT NOT NULL, 
		DATE INTEGER NOT NULL, 
		ATTACHMENTS BLOB NOT NULL, 
		AUTHOR TXT NOT NULL, 
		CATEGORY TEXT NOT NULL)''')
	#cursor.execute('''INSERT INTO LESSONS (TITLE, CONTENT, DATE, ATTACHMENTS, AUTHOR, CATEGORY) VALUES ("lesson 1", "xdddd", 0, ?, "admin", "jp2")''', (dumps(["j.png", "p.mp4", "2.mp3"]),))
	conn.commit()
	conn.close()

# create ARTICLES with one example
if 0:
	conn = sqlite3.connect("db.db")
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE ARTICLES (ID INTEGER PRIMARY KEY AUTOINCREMENT,
		TITLE TEXT NOT NULL,
		CONTENT TEXT NOT NULL,
		BRIEF TEXT NOT NULL,
		DATE INTEGER NOT NULL,
		ATTACHMENTS BLOB NOT NULL,
		AUTHOR TXT NOT NULL,
		CATEGORY TEXT NOT NULL)''')
	cursor.execute('''INSERT INTO ARTICLES (TITLE, CONTENT, BRIEF, DATE, ATTACHMENTS, AUTHOR, CATEGORY) VALUES ("JP", "wiadomo ktory drgccgdtgtdfgdtrcgdcrgcdr", "kotki opis", 0, ?, "admin", "69")''', (dumps(["4.png", "2.mp4", "0.mp3"]),))
	conn.commit()
	conn.close()


if 0:
	conn = sqlite3.connect("db.db")
	cursor = conn.cursor()
	cursor.execute("DROP TABLE LESSONS")
	cursor.execute('''CREATE TABLE LESSONS (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
		TITLE TEXT NOT NULL, 
		CONTENT TEXT NOT NULL, 
		DATE INTEGER NOT NULL, 
		ATTACHMENTS BLOB NOT NULL, 
		AUTHOR TXT NOT NULL, 
		CATEGORY TEXT NOT NULL)''')
	#cursor.execute('''INSERT INTO LESSONS (TITLE, CONTENT, DATE, ATTACHMENTS, AUTHOR, CATEGORY) VALUES ("lesson 1", "xdddd", 0, ?, "admin", "jp2")''', (dumps(["j.png", "p.mp4", "2.mp3"]),))
	conn.commit()
	conn.close()






#conn = sqlite3.connect('db.db')
#
#c = conn.cursor()
#c.execute('''CREATE TABLE USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT, USER TEXT NOT NULL, PASSWORD TEXT NOT NULL);''')
#c.execute('''CREATE TABLE POSTS (ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT NOT NULL, CONTENT TEXT NOT NULL);''')  # tu nie powinno byc jeszcze daty tez? i zalacznika i autora?

#c.execute('''CREATE TABLE LESSONS (ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT NOT NULL, CONTENT TEXT NOT NULL, DATE TEXT NOT NULL, ATTACHMENT TEXT NOT NULL, AUTHOR TXT NOT NULL, CATEGORY TEXT NOT NULL );''')
#c.execute('''CREATE TABLE ARTICLES (ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT NOT NULL, CONTENT TEXT NOT NULL, DATE TEXT NOT NULL, ATTACHMENT TEXT NOT NULL, AUTHOR TXT NOT NULL, CATEGORY TEXT NOT NULL );''')
#c.execute('''CREATE TABLE ZAGRYWKA (ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT NOT NULL, CONTENT TEXT NOT NULL, DATE TEXT NOT NULL, ATTACHMENT TEXT NOT NULL, AUTHOR TXT NOT NULL, METRUM TEXT NOT NULL, TEMPO TEXT NOT NULL, TYPE TEXT NOT NULL, DIFFICULTY TEXT NOT NULL  );''')


#c.execute("""INSERT INTO USERS (USER, PASSWORD) VALUES ('John420', 'password123');""")
#c.execute("""DELETE FROM USERS WHERE ID = 3""")

#c.execute("""INSERT INTO POSTS (TITLE, CONTENT) VALUES ('Post1', 'Content of post 1');""")
#c.execute("""INSERT INTO POSTS (TITLE, CONTENT) VALUES ('Post2', 'Content of post 2');""")
#c.execute("""INSERT INTO POSTS (TITLE, CONTENT) VALUES ('Post3', 'Content of post 3');""")
#c.execute("""INSERT INTO POSTS (TITLE, CONTENT) VALUES ('Post4', 'Content of post 4');""")
#c.execute("""INSERT INTO LESSONS (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, CATEGORY) VALUES ('Lekcja1', 'Content of lesson 1', '2023-01-02 20:30', '', 'John420', 'rock');""")
#c.execute("""INSERT INTO LESSONS (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, CATEGORY) VALUES ('Lekcja2', 'Content of lesson 2', '2023-02-01 19:30', '', 'xxx15', 'modern');""")
#c.execute("""INSERT INTO LESSONS (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, CATEGORY) VALUES ('Lekcja3', 'Content of lesson 3', '2023-03-03 18:30', '', 'lol84', 'pop');""")
#c.execute("""INSERT INTO LESSONS (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, CATEGORY) VALUES ('Lekcja4', 'Content of lesson 4', '2023-04-04 17:30', '', 'filip123', 'alternative');""")
#c.execute("""INSERT INTO ARTICLES (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, CATEGORY) VALUES ('Artykul1', 'Content of article 1', '2023-01-02 20:30', '', 'John420', 'rock');""")
#c.execute("""INSERT INTO ARTICLES (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, CATEGORY) VALUES ('Artykul2', 'Content of article 2', '2023-02-01 19:30', '', 'xxx15', 'modern');""")
#c.execute("""INSERT INTO ARTICLES (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, CATEGORY) VALUES ('Artykul3', 'Content of article 3', '2023-03-03 18:30', '', 'lol84', 'pop');""")
#c.execute("""INSERT INTO ARTICLES (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, CATEGORY) VALUES ('Artykul4', 'Content of article 4', '2023-04-04 17:30', '', 'filip123', 'alternative');""")
#c.execute("""INSERT INTO ZAGRYWKA (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, METRUM, TEMPO, TYPE, DIFFICULTY) VALUES ('Artykul1', 'Content of article 1', '2023-01-02 20:30', '', 'John420', '3/5', '100bpm', 'rock', 'easy');""")
#c.execute("""INSERT INTO ZAGRYWKA (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, METRUM, TEMPO, TYPE, DIFFICULTY) VALUES ('Artykul2', 'Content of article 2', '2023-02-01 19:30', '', 'xxx15', '2/3', '120bpm', 'pop', 'hard');""")
#c.execute("""INSERT INTO ZAGRYWKA (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, METRUM, TEMPO, TYPE, DIFFICULTY) VALUES ('Artykul3', 'Content of article 3', '2023-03-03 18:30', '', 'lol84', '1/4', '200bpm', 'modern', 'normal');""")
#c.execute("""INSERT INTO ZAGRYWKA (TITLE, CONTENT, DATE, ATTACHMENT, AUTHOR, METRUM, TEMPO, TYPE, DIFFICULTY) VALUES ('Artykul4', 'Content of article 4', '2023-04-04 17:30', '', 'filip123', '2/4', '80bpm', 'jazz', 'easy');""")


# commit
#conn.commit()

# close the connection
#conn.close()


#conn = sqlite3.connect('db.db')
#cursor = conn.cursor()

#cursor.execute("""DELETE FROM POSTS WHERE ID > 0""")

#cursor.execute("DROP TABLE POSTS")
#cursor.execute('''CREATE TABLE USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT, LOGIN TEXT NOT NULL, PASSWORD TEXT NOT NULL, TYPE TEXT NOT NULL, BAN INTEGER NOT NULL, FRIENDS BLOB NOT NULL);''')
#cursor.execute('''CREATE TABLE POSTS (ID INTEGER PRIMARY KEY AUTOINCREMENT, TITLE TEXT NOT NULL,  CONTENT TEXT NOT NULL,  DATE INTEGER NOT NULL, VISIBLE INTEGER NOT NULL, ATTACHMENT TEXT NOT NULL, AUTHOR TEXT NOT NULL);''')
#cursor.execute("""INSERT INTO POSTS (TITLE, CONTENT, DATE, VISIBLE, ATTACHMENT, AUTHOR) VALUES ("Post nr 1", "Content of post 1", 0, 1, "postAttachment/1.png", "admin");""")
#cursor.execute("""INSERT INTO POSTS (TITLE, CONTENT, DATE, VISIBLE, ATTACHMENT, AUTHOR) VALUES ("Post nr 2", "Content of post 2. Only for logged in", 0, 0, "postAttachment/2.png", "admin");""")

#import json
#my_json = "[1, 2, 3]"
#my_array = json.loads(my_json)
#cursor.execute("""INSERT INTO USERS (LOGIN, PASSWORD, TYPE, BAN, FRIENDS) VALUES ('admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'admin', 0, ?);""", (json.dumps(my_array),))
#print(x.description)

#conn.commit()
#conn.close()