from sqlite3 import connect
from models.templates import Render
from json import dumps


def handleRequest(Request):
	if Request.userID == -1:
		return Render.responseJSON('{"status": "Access denied"}')
	try:
		conn = connect("models/db.db")
		cursor = conn.cursor()
		cursor.execute("SELECT ID, TITLE, BRIEF, DATE, AUTHOR, CATEGORY FROM LESSONS")
		data = cursor.fetchall()
		conn.close()
		return Render.responseJSON(dumps({"status": "OK", "data": [{"id": x[0], "title": x[1], "brief": x[2], "date": x[3], "author": x[4], "category": x[5]} for x in reversed(data)]}))
	except:
		return Render.responseJSON('{"status": "ERR"}')