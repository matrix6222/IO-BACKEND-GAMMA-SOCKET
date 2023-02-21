from json import loads
from sqlite3 import connect
from models.templates import Render
from hashlib import sha256


def handleRequest(Request):
	try:
		JSON = loads(Request.payload)
	except:
		return Render.responseJSON('{"status": "Invalid json"}')
	if not ("login" in JSON and "password" in JSON):
		return Render.responseJSON('{"status": "Invalid field in json"}')
	conn = connect("models/db.db")
	cursor = conn.cursor()
	cursor.execute("""SELECT ID, PASSWORD, TYPE, BAN FROM USERS WHERE LOGIN = ?""", (JSON["login"],))
	data = cursor.fetchall()
	conn.close()
	if len(data) != 1:
		return Render.responseJSON('{"status": "User not found"}')
	dbID, dbPassword, dbType, dbBan = data[0][0], data[0][1], data[0][2], data[0][3]
	if dbBan == 1:
		return Render.responseJSON('{"status": "User banned"}')
	if sha256(JSON["password"]).hexdigest() != dbPassword:
		return Render.responseJSON('{"status": "Incorrect password"}')
	cookie = Request.cookies.findUserCookie(JSON["login"])
	if cookie == "":
		newCookie = Request.cookies.add(dbID, JSON["login"], dbType)
		return Render.responseJSONwithSetCookie('{"status": "OK"}', newCookie)
	else:
		return Render.responseJSONwithSetCookie('{"status": "OK"}', cookie)