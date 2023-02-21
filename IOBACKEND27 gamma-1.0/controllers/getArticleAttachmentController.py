from models.filesManagement import FilesManagment
from models.templates import Render
from os import path


def handleRequest(Request):
	fileExtension = '.png' if Request.url.find('.png') != -1 else '.mp4' if Request.url.find('.mp4') != -1 else '.mp3' if Request.url.find('.mp3') != -1 else '.pdf' if Request.url.find('.pdf') != -1 else ''
	if fileExtension == '':
		return Render.responseERROR()
	return FilesManagment.getFile(Request.url[19: Request.url.find(fileExtension)], fileExtension, path.join(Request.path, "views", "articlesAttachments"), Request)