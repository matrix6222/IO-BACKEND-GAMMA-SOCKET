from models.templates import Render


def handleRequest(Request):
	return Render.responseJSON('{"status": "OK", "userName": "' + Request.userName + '"}')