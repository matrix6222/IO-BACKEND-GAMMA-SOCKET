from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from models.sessions import Session
from models.request import Request
from os import path, pardir


class ServerHTTP:
	def __init__(self):
		self.path = path.abspath(path.join(path.dirname(path.abspath(__file__)), pardir))
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind(("", 25565))
		self.urlsCheck = []
		self.urlsModule = []
		self.cookies = Session()
		data = [[y.strip() for y in x.split(" ")] for x in open(path.join(self.path, "endpointsConfiguration.txt"), "r").read().split("\n") if x != "" and x != "\n" and x != " " and x.count(" ") == 2]
		for x in data:
			print(x)
			self.urlsCheck.append(x[0] + " " + x[1])
			package = __import__("controllers." + x[2])
			module = getattr(package, x[2])
			self.urlsModule.append(module)

	def processRequest(self, req, conn, handleModule):
		res = handleModule.handleRequest(req)
		conn.send(res)
		conn.close()

	def run(self):
		self.sock.listen(128)
		while True:
			try:
				conn, addr = self.sock.accept()
				req = conn.recv(10485760)
				try:
					x = self.urlsCheck.index(req[:req.find(" HTTP")] if req[:req.find(" HTTP")].find("/", req.find("/") + 1) == -1 else req[:req.find("/", req.find("/") + 1)])
					print(req)
					Thread(target=self.processRequest, args=(Request(req, conn, addr, self.cookies, self.path), conn, self.urlsModule[x])).start()
				except:
					conn.send("HTTP/1.1 404 Not Found\r\n\r\n")
					conn.close()
			except:
				print("server erorr")
