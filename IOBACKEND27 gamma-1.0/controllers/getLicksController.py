from sqlite3 import connect
from models.templates import Render
from json import dumps, loads


def handleRequest(Request):
	if Request.userID == -1:
		return Render.responseJSON('{"status": "Access denied"}')
	try:
		conn = connect("models/db.db")
		cursor = conn.cursor()
		cursor.execute("SELECT ID, TITLE, CONTENT, BRIEF, DATE, ATTACHMENTS, AUTHOR, BEAT, TEMPO, TYPE, DIFFICULTY FROM LICKS")
		data = cursor.fetchall()
		conn.close()
		return Render.responseJSON(dumps({"status": "OK", "data": [{"id": x[0], "title": x[1], "content": x[2], "brief": x[3], "date": x[4], "attachments": loads(x[5]), "author": x[6], "beat": x[7], "tempo": x[8], "type": x[9], "difficulty": x[10]} for x in reversed(data)]}))
	except:
		return Render.responseJSON('{"status": "ERR"}')