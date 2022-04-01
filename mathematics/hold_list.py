"""Holds a list, so it can be accessed when python quits"""
import os
import platform
import mathematics


class HoldList:
	"""
	Holds a list, so it can be accessed after python quits and starts again.
	"""

	def __init__(self, name):
		"""
		:param name: The name of the file, starts in the default directory
		"""
		self.file_name = name
		try:
			if platform.system() == "Windows":
				self.path = "C:/Users/" + str(
					os.getlogin()) + "/AppData/Local/Temp/mathematics-python/" + mathematics.VERSION + "/"
			elif platform.system() == "Darwin":
				self.path = "~/Library/Application Support/mathematics-python/" + mathematics.VERSION + "/"
			elif platform.system() == "Linux":
				self.path = "~/.mathematics-python/" + mathematics.VERSION + "/"
			else:
				self.path = ""
			f = open(self.path + self.file_name + ".list", "r")
			self.hold = f.read()
			f.close()
		except FileNotFoundError:
			self.hold = ""
			self.save()

	def delete(self):
		"""Deletes the object, should be used with del"""
		import os

		os.remove(self.path + self.file_name + ".list")

	def save(self):
		"""Saves hold"""
		f = open(self.path + self.file_name + ".list", "w")
		f.write(str(self.hold)[1: len(self.hold) - 2])
		f.close()

	def read(self):
		"""
		Returns the contents of the file
		:return:
		"""
		f = open(self.path + self.file_name + ".list", "r")
		contents = f.read().split(", ")
		f.close()
		return contents

	def modify(self, new):
		self.hold = new
