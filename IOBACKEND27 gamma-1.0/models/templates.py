from os import path, pardir
frontendAddress = open(path.abspath(path.join(path.dirname(path.abspath(__file__)), pardir, "frontendAddress.txt")), "r").read().strip()      # TODO delete in release
ssl = 1 if open(path.abspath(path.join(path.dirname(path.abspath(__file__)), pardir, "sslEnable.txt")), "r").read().strip() == "True" else 0  # TODO delete in release


class Render:

	@staticmethod
	def responseJSON(json):
		return "HTTP/1.1 200 OK\r\nAccess-Control-Allow-Origin: {}\r\nAccess-Control-Allow-Credentials: true\r\nContent-Type: application/json\r\nContent-Length: {}\r\n\r\n{}".format(frontendAddress, len(json), json)

	@staticmethod
	def responseJSONwithSetCookie(json, cookie):
		return "HTTP/1.1 200 OK\r\nAccess-Control-Allow-Origin: {}\r\nAccess-Control-Allow-Credentials: true\r\nSet-Cookie: authentication=\"{}\"{}\r\nContent-Type: application/json\r\nContent-Length: {}\r\n\r\n{}".format(frontendAddress, cookie, "; Domain=light.one.pl; SameSite=None; Secure" if ssl else "", len(json), json)

	@staticmethod
	def responseERROR():
		return "HTTP/1.1 404 Not Found\r\n\r\n"

	@staticmethod
	def responsePNG(png):
		return "HTTP/1.1 200 OK\r\nAccess-Control-Allow-Origin: {}\r\nAccess-Control-Allow-Credentials: true\r\nContent-Type: image/png\r\nContent-Length: {}\r\n\r\n{}".format(frontendAddress, len(png), png)

	@staticmethod
	def responsePDF(pdf):
		return "HTTP/1.1 200 OK\r\nAccess-Control-Allow-Origin: {}\r\nAccess-Control-Allow-Credentials: true\r\nContent-Type: application/pdf\r\nContent-Length: {}\r\n\r\n{}".format(frontendAddress, len(pdf), pdf)

	@staticmethod
	def responseMP4(mp4Part, start, allDataLenght):
		return "HTTP/1.1 206 Partial Content\r\nAccess-Control-Allow-Origin: {}\r\nAccess-Control-Allow-Credentials: true\r\nContent-Type: video/mp4\r\nAccept-Ranges: bytes\r\nContent-Length: {}\r\nContent-Range: bytes {}-{}/{}\r\n\r\n{}".format(frontendAddress, allDataLenght, start, allDataLenght - 1, allDataLenght, mp4Part)

	@staticmethod
	def responseMP4Accept():
		return "HTTP/1.1 200 OK\r\nAccess-Control-Allow-Origin: {}\r\nAccess-Control-Allow-Credentials: true\r\nContent-Type: video/mp4\r\nAccept-Ranges: bytes\r\n\r\n".format(frontendAddress)

	@staticmethod
	def responseMP3(mp4Part, start, allDataLenght):
		return "HTTP/1.1 206 Partial Content\r\nAccess-Control-Allow-Origin: {}\r\nAccess-Control-Allow-Credentials: true\r\nContent-Type: audio/mpeg\r\nAccept-Ranges: bytes\r\nContent-Length: {}\r\nContent-Range: bytes {}-{}/{}\r\n\r\n{}".format(frontendAddress, allDataLenght, start, allDataLenght - 1, allDataLenght, mp4Part)

	@staticmethod
	def responseMP3Accept():
		return "HTTP/1.1 200 OK\r\nAccess-Control-Allow-Origin: {}\r\nAccess-Control-Allow-Credentials: true\r\nContent-Type: audio/mpeg\r\nAccept-Ranges: bytes\r\n\r\n".format(frontendAddress)
