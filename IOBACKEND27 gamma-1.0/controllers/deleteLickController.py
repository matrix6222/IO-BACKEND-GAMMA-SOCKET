from sqlite3 import connect
from models.templates import Render
from json import loads
from models.filesManagement import FilesManagment
from os import path


def handleRequest(Request):
	if Request.userID == -1:
		return Render.responseJSON('{"status": "Access denied"}')
	try:
		JSON = loads(Request.payload)
	except:
		return Render.responseJSON('{"status": "Invalid json"}')
	if not "id" in JSON:
		return Render.responseJSON('{"status": "Invalid field in json"}')
	try:
		id = int(JSON["id"])
	except:
		return Render.responseJSON('{"status": "Invalid id"}')
	conn = connect("models/db.db")
	cursor = conn.cursor()
	cursor.execute("SELECT ATTACHMENTS, AUTHOR FROM LICKS WHERE ID = ?", (id,))
	data = cursor.fetchall()
	if len(data) != 1:
		conn.close()
		return Render.responseJSON('{"status": "Lick not exist"}')
	if data[0][1] != Request.userName and Request.userType != 'admin':
		conn.close()
		return Render.responseJSON('{"status": "Access denied"}')
	cursor.execute('''DELETE FROM LICKS WHERE ID = ?''', (id,))
	conn.commit()
	conn.close()
	FilesManagment.deleteFiles(loads(data[0][0]), path.join(Request.path, "views", "licksAttachments"))
	return Render.responseJSON('{"status": "OK"}')