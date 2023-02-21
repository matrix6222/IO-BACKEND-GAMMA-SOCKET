from models.templates import Render
from json import loads
from sqlite3 import connect
from hashlib import sha256


def handleRequest(Request):
	try:
		JSON = loads(Request.payload)
	except:
		return Render.responseJSON('{"status": "Invalid json"}')
	if not ("password" in JSON and "newPassword" in JSON):
		return Render.responseJSON('{"status": "Invalid field in json"}')
	login = Request.userName
	if login == '':
		return Render.responseJSON('{"status": "ERR"}')
	if len(JSON["newPassword"]) < 8:
		return Render.responseJSON('{"status": "Password is to short"}')
	conn = connect("models/db.db")
	cursor = conn.cursor()
	cursor.execute("""SELECT PASSWORD FROM USERS WHERE LOGIN = ?""", (login,))
	data = cursor.fetchall()
	if len(data) != 1:
		conn.close()
		return Render.responseJSON('{"status": "User not found"}')
	if sha256(JSON["password"]).hexdigest() != data[0][0]:
		return Render.responseJSON('{"status": "Incorrect password"}')
	cursor.execute("""UPDATE USERS SET PASSWORD = ? WHERE LOGIN = ?""", (sha256(JSON["newPassword"]).hexdigest(), login,))
	conn.commit()
	conn.close()
	return Render.responseJSON('{"status": "OK"}')