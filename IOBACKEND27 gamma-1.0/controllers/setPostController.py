from sqlite3 import connect
from models.templates import Render
from json import loads, dumps
from os import path
from time import time

from models.filesManagement import FilesManagment


def handleRequest(Request):
	if not Request.userType in ["admin", "amateur", "proUnverified", "pro"]:
		return Render.responseJSON('{"status": "Access denied"}')
	try:
		JSON = loads(Request.payload)
	except:
		return Render.responseJSON('{"status": "Invalid json"}')
	if not ("title" in JSON and "content" in JSON and "public" in JSON and "attachments" in JSON):
		return Render.responseJSON('{"status": "Invalid field in json"}')
	if not JSON["public"] in [0, 1]:
		return Render.responseJSON('{"status": "Public must be 0 or 1"}')
	if len(JSON["attachments"]) > 1:
		return Render.responseJSON('{"status": "0 or 1 attachments"}')
	status, files, extensions = FilesManagment.base64ToBytes(JSON["attachments"])
	if status == False:
		return Render.responseJSON('{"status": "Invalid file"}')
	newFileNames = FilesManagment.saveFiles(files, extensions, path.join(Request.path, "views", "postsAttachments"))
	conn = connect("models/db.db")
	cursor = conn.cursor()
	cursor.execute('''INSERT INTO POSTS (TITLE, CONTENT, DATE, PUBLIC, ATTACHMENTS, AUTHOR) VALUES (?, ?, ?, ?, ?, ?);''', (JSON["title"], JSON["content"], int(time()), JSON["public"], dumps(newFileNames), Request.userName))
	conn.commit()
	conn.close()
	return Render.responseJSON('{"status": "OK"}')
