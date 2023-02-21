from hashlib import sha256
from random import randint

class Session:
	def __init__(self):
		self.dict = {}

	def add(self, userID, userName, userType):
		newCookie = sha256(str(randint(0, 99999999999999999999999999999999999999999999999999999999))).hexdigest()
		while newCookie in self.dict.keys():
			newCookie = sha256(str(randint(0, 99999999999999999999999999999999999999999999999999999999))).hexdigest()
		self.dict[newCookie] = [userID, userName, userType]
		return newCookie

	def get(self, cookie):
		if cookie in self.dict:
			return self.dict[cookie]
		else:
			return [-1, '', 'guest']

	def remove(self, cookie):
		if cookie in self.dict:
			del self.dict[cookie]

	def findUserCookie(self, userName):
		for key, item in self.dict.items():
			if item[1] == userName:
				return key
		return ""

	def changeUserType(self, userName, newUserType):
		if newUserType in ["admin", "amateur", "proUnverified", "pro", "guest"]:
			for key, item in self.dict.items():
				if item[1] == userName:
					self.dict[key] = [item[0], item[1], newUserType]
					return 2
			return 1
		else:
			return 0