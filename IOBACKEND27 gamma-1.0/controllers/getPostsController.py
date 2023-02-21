from sqlite3 import connect
from models.templates import Render
from json import dumps, loads


def handleRequest(Request):
	conn = connect("models/db.db")
	cursor = conn.cursor()
	cursor.execute("SELECT ID, TITLE, CONTENT, DATE, ATTACHMENTS, AUTHOR FROM POSTS WHERE PUBLIC = 1" if Request.userID == -1 else "SELECT ID, TITLE, CONTENT, DATE, ATTACHMENTS, AUTHOR FROM POSTS")
	data = cursor.fetchall()
	conn.close()
	return Render.responseJSON(dumps({"status": "OK", "data": [{"id": x[0], "title": x[1], "content": x[2], "date": x[3], "attachments": loads(x[4]), "author": x[5]} for x in reversed(data)]}))
