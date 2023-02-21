from base64 import b64decode
from random import choice
from os import listdir, path, remove
from models.templates import Render


class FilesManagment:

	@staticmethod
	def base64ToBytes(base64Files):
		files, extensions, = [], []
		for base64File in base64Files:
			if base64File.startswith("data:image/png;base64,"):
				data = b64decode(base64File[22:])
				if data[:8] != '\x89PNG\r\n\x1a\n':
					return (False, [], [])
				else:
					files.append(data)
					extensions.append(".png")
			elif base64File.startswith("data:audio/mpeg;base64,"):
				data = b64decode(base64File[23:])
				if data[:2] != "\xff\xfb" and data[:3] != "\x49\x44\x33":
					return (False, [], [])
				else:
					files.append(data)
					extensions.append(".mp3")
			elif base64File.startswith("data:video/mp4;base64,"):
				data = b64decode(base64File[22:])
				if not data[4:12] in ["ftypmmp4", "ftypmp41", "ftypmp42"]:
					return (False, [], [])
				else:
					files.append(data)
					extensions.append(".mp4")
			elif base64File.startswith("data:application/pdf;base64,"):
				data = b64decode(base64File[28:])
				if not data[:7] in ["%PDF-1.", "%PDF-2."]:
					return (False, [], [])
				else:
					files.append(data)
					extensions.append(".pdf")
			else:
				return (False, [], [])
		return (True, files, extensions)

	@staticmethod
	def saveFiles(files, extensions, pathToDir):
		existingFiles, newFileNames = listdir(pathToDir), []
		for y in range(len(files)):
			newFile = "".join([choice("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM") for x in range(15)]) + extensions[y]
			while newFile in existingFiles:
				newFile = "".join([choice("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM") for x in range(15)]) + extensions[y]
			newFileNames.append(newFile)
			file = open(path.join(pathToDir, newFile), "wb")
			file.write(files[y])
			file.close()
		return newFileNames

	@staticmethod
	def deleteFiles(files, pathToDir):
		for fileName in files:
			pathToFile = path.join(pathToDir, fileName)
			if path.isfile(pathToFile):
				remove(pathToFile)

	@staticmethod
	def getFile(fileName, fileExtension, pathToDir, Request):
		if not fileName + fileExtension in listdir(pathToDir):
			return Render.responseERROR()
		if fileExtension == ".png":
			file = open(path.join(pathToDir, fileName + fileExtension), "rb")
			png = file.read()
			file.close()
			return Render.responsePNG(png)
		elif fileExtension == ".mp4":
			if not "Range" in Request.headers:
				return Render.responseMP4Accept()
			else:
				try:
					startByte = int(Request.headers["Range"][6:-1])
					file = open(path.join(pathToDir, fileName + fileExtension), "rb")
					mp4 = file.read()
					file.close()
					return Render.responseMP4(mp4[startByte:], startByte, len(mp4))
				except:
					Render.responseERROR()
		elif fileExtension == ".mp3":
			if not "Range" in Request.headers:
				return Render.responseMP3Accept()
			else:
				try:
					startByte = int(Request.headers["Range"][6:-1])
					file = open(path.join(pathToDir, fileName + fileExtension), "rb")
					mp3 = file.read()
					file.close()
					return Render.responseMP3(mp3[startByte:], startByte, len(mp3))
				except:
					Render.responseERROR()
		elif fileExtension == ".pdf":
			file = open(path.join(pathToDir, fileName + fileExtension), "rb")
			pdf = file.read()
			file.close()
			return Render.responsePDF(pdf)
		else:
			return Render.responseERROR()