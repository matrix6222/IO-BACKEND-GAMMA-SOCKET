from json import loads
from sqlite3 import connect
from models.templates import Render
from hashlib import sha256


def handleRequest(Request):
	try:
		JSON = loads(Request.payload)
	except:
		return Render.responseJSON('{"status": "Invalid json"}')
	if not ("login" in JSON and "email" in JSON and "password" in JSON and "type" in JSON):
		return Render.responseJSON('{"status": "Invalid field in json"}')
	if len(JSON["login"]) < 6 and not JSON["login"] == 'admin':
		return Render.responseJSON('{"status": "Login is too short"}')
	if not JSON["login"].isalnum():
		return Render.responseJSON('{"status": "Login contains unallowed character"}')
	if len(JSON["password"]) < 8:
		return Render.responseJSON('{"status": "Password is to short"}')
	if not JSON["type"] in ["amateur", "pro"]:
		return Render.responseJSON('{"status": "Incorrect account type"}')
	conn = connect("models/db.db")
	cursor = conn.cursor()
	cursor.execute("""SELECT LOGIN, EMAIL FROM USERS""")
	data = cursor.fetchall()
	if [JSON["login"], JSON["email"]] in data:
		conn.close()
		return Render.responseJSON('{"status": "User already exist"}')
	cursor.execute("""INSERT INTO USERS (LOGIN, EMAIL, PASSWORD, TYPE, BAN) VALUES (?, ?, ?, ?, ?);""", (JSON["login"], JSON["email"], sha256(JSON["password"]).hexdigest(), 'amateur' if JSON["type"] == 'amateur' else 'proUnverified', 0))
	conn.commit()
	conn.close()
	return Render.responseJSON('{"status": "OK"}')