from sqlite3 import connect
from models.templates import Render
from json import dumps, loads


def handleRequest(Request):
	if Request.userID == -1:
		return Render.responseJSON('{"status": "Access denied"}')
	try:
		JSON = loads(Request.payload)
		if not "id" in JSON:
			return Render.responseJSON('{"status": "ERR"}')
		id = int(JSON["id"])
		conn = connect("models/db.db")
		cursor = conn.cursor()
		cursor.execute("SELECT ID, TITLE, CONTENT, DATE, ATTACHMENTS, AUTHOR, CATEGORY FROM LESSONS WHERE ID = ?", (id,))
		data = cursor.fetchall()
		conn.close()
		return Render.responseJSON(dumps({"status": "OK", "data": [{"id": x[0], "title": x[1], "content": x[2], "date": x[3], "attachments": loads(x[4]), "author": x[5], "category": x[6]} for x in data]}))
	except:
		return Render.responseJSON('{"status": "ERR"}')