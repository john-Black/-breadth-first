class Path2:
	def __init__(self, name, br = []):
		self.node = name
		self.tree = br + [name]


	def addPathVertex(self, nod):
		self.tree.append(nod)


	def getPath(self):
		return self.tree


	def __str__(self):
		return str(self.node)

	def __repr__(self):
		return self.node

	def getName(self):
		return self.node

	def setPath(self, aw):
		self.tree = aw
