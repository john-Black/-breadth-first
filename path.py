class Path:
	def __init__(self,anw,  ans = None):
		self.direc = [anw, ans]
		if ans == None:
			self.direc = [anw]
		else:
			self.direc = [anw, ans]
		self.tree = {}


	def addPathVertex(self, nod):
		self.direc.append(nod)

	def explored(self, nod):
		if nod in self.direc:
			return True
		else:
			return False

	def getPath(self):
		return list(reversed(self.direc))

	def getDistance(self):
		return len(self.direc)

	def __str__(self):
		return str(list(reversed(self.direc)))

	def setTree(self, aw):
		self.tree = aw
    
