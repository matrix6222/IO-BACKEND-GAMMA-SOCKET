from models.templates import Render
from models.filesManagement import FilesManagment
from os import path
from sqlite3 import connect
from json import loads


def handleRequest(Request):
	fileExtension = '.png' if Request.url.find('.png') != -1 else '.mp4' if Request.url.find('.mp4') != -1 else '.mp3' if Request.url.find('.mp3') != -1 else '.pdf' if Request.url.find('.pdf') != -1 else ''
	if fileExtension == '':
		return Render.responseERROR()
	return FilesManagment.getFile(Request.url[18: Request.url.find(fileExtension)], fileExtension, path.join(Request.path, "views", "lessonsAttachments"), Request)