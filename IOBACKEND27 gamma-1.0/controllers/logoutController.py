from models.templates import Render


def handleRequest(Request):
	Request.cookies.remove(Request.cookie)
	return Render.responseJSON('{"status": "OK"}')
