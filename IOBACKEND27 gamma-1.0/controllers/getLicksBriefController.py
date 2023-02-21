from sqlite3 import connect
from models.templates import Render
from json import dumps, loads


def handleRequest(Request):
	if Request.userID == -1:
		return Render.responseJSON('{"status": "Access denied"}')
	try:
		conn = connect("models/db.db")
		cursor = conn.cursor()
		cursor.execute("SELECT ID, TITLE, BRIEF, DATE, AUTHOR, BEAT, TEMPO, TYPE, DIFFICULTY FROM LICKS")
		data = cursor.fetchall()
		conn.close()
		return Render.responseJSON(dumps({"status": "OK", "data": [{"id": x[0], "title": x[1], "brief": x[2], "date": x[3], "author": x[4], "beat": x[5], "tempo": x[6], "type": x[7], "difficulty": x[8]} for x in reversed(data)]}))
	except:
		return Render.responseJSON('{"status": "ERR"}')