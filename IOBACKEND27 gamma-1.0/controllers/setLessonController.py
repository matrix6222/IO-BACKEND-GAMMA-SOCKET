from sqlite3 import connect
from models.templates import Render
from json import loads, dumps
from os import path
from time import time

from models.filesManagement import FilesManagment


def handleRequest(Request):
	if not Request.userType in ["admin", "pro"]:
		return Render.responseJSON('{"status": "Access denied"}')
	try:
		JSON = loads(Request.payload)
	except:
		return Render.responseJSON('{"status": "Invalid json"}')
	if not ("title" in JSON and "content" in JSON and "attachments" in JSON and "brief" in JSON and "category" in JSON):
		return Render.responseJSON('{"status": "Invalid field in json"}')
	status, files, extensions = FilesManagment.base64ToBytes(JSON["attachments"])
	if status == False:
		return Render.responseJSON('{"status": "Invalid file"}')
	newFileNames = FilesManagment.saveFiles(files, extensions, path.join(Request.path, "views", "lessonsAttachments"))
	conn = connect("models/db.db")
	cursor = conn.cursor()
	cursor.execute('''INSERT INTO LESSONS (TITLE, CONTENT, BRIEF, DATE, ATTACHMENTS, AUTHOR, CATEGORY) VALUES (?, ?, ?, ?, ?, ?, ?);''', (JSON["title"], JSON["content"], JSON["brief"], int(time()), dumps(newFileNames), Request.userName, JSON["category"]))
	conn.commit()
	conn.close()
	return Render.responseJSON('{"status": "OK"}')