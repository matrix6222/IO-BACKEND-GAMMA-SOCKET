class Request:
	def __init__(self, req, conn, addr, cookies, path):
		self.method = ""
		self.url = ""
		self.headers = {}
		self.payload = req[req.find("\r\n\r\n") + 4:]
		self.address = addr
		self.userID = -1
		self.userName = ''
		self.userType = 'guest'
		self.cookie = ''
		self.cookies = cookies
		self.path = path
		data = req[0: req.find("\r\n\r\n")].split("\r\n")
		for x in data[1:]:
			k, v = x.split(": ")
			self.headers[k] = v
		self.method, self.url, _ = data[0].split(" ")
		if "Content-Length" in self.headers:
			try:
				targetLen = int(self.headers["Content-Length"])
				if targetLen != 0:
					while len(self.payload) != targetLen:
						self.payload += conn.recv(10485760)
			except:
				pass
		if "Cookie" in self.headers:
			data = self.headers["Cookie"]
			start = data.find('authentication="')
			if start != -1:
				self.cookie = data[start + 16:data.find('"', start + 16)]
				IDNameType = cookies.get(self.cookie)
				self.userID = IDNameType[0]
				self.userName = IDNameType[1]
				self.userType = IDNameType[2]
