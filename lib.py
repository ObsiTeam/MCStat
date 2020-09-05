import sys
import os
class fore:
	def __init__(self, r, g, b, text):
		self.go = ""
		self.r = str(r)
		self.g = str(g)
		self.b = str(b)
		sys.stdout.write ("\x1b[38;2;"+str(r)+";"+str(g)+";"+str(b)+"m"+text)

class back:
	def __init__(self, r, g, b,text):
		self.go = ""
		self.r = str(r)
		self.g = str(g)
		self.b = str(b)
		sys.stdout.write ("\x1b[48;2;"+str(r)+";"+str(g)+";"+str(b)+"m"+text)

class cls:
	try: os.system("cls")
	except: os.system("clear")

class color:
	def __init__(self,color): os.system("color "+color)

class reset:
	go = ""
	sys.stdout.write('\x1B[40m')
