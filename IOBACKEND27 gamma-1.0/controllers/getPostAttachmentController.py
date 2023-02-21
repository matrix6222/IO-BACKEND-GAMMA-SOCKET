from models.templates import Render
from models.filesManagement import FilesManagment
from os import path
from sqlite3 import connect
from json import loads


def handleRequest(Request):
	fileExtension = '.png' if Request.url.find('.png') != -1 else '.mp4' if Request.url.find('.mp4') != -1 else '.mp3' if Request.url.find('.mp3') != -1 else '.pdf' if Request.url.find('.pdf') != -1 else ''
	if fileExtension == '':
		return Render.responseERROR()
	fileName = Request.url[16: Request.url.find(fileExtension)]
	if Request.userID == -1:
		conn = connect("models/db.db")
		cursor = conn.cursor()
		cursor.execute("""SELECT ATTACHMENTS FROM POSTS WHERE PUBLIC = 1""")
		data = cursor.fetchall()
		conn.close()
		if not fileName + fileExtension in sum([loads(x[0]) for x in data], []):
			return Render.responseERROR()
		return FilesManagment.getFile(fileName, fileExtension, path.join(Request.path, "views", "postsAttachments"), Request)
	else:
		return FilesManagment.getFile(fileName, fileExtension, path.join(Request.path, "views", "postsAttachments"), Request)
