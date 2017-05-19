from path import Path
from path2 import Path2

class BreadthFirst:
	def __init__(self, ver = {}):
		self.expl = []
		self.nodes = ver


	def run(self, first, last):
		self.expl = []
		pa = Path2(first)
		sa = {pa: self.getNeighbors(pa)}
		return self.gotoF(first, last, sa)

	def gotoF(self, key, find, arr):
		va, pa = self.BfsIter(key, find, arr)

		if pa == None:
			return self.gotoF(key, find, va)

		else:
			return va, pa



	def BfsIter(self, key, find, arr):
		if key not in self.expl:
			self.expl.append(key)

		sav = None
		g = {}

		if arr == None:
			return arr, sav

		for k, a in arr.items():
			if type(a) == type({}):
				v, res = self.BfsIter(k, find, a)
				if res != None and sav == None:
					sav = res
			else:
				info = self.inList(find, a)
				if info != None:
					return arr, info
				else:
					arr[k] = self.getNodes(a)

		return arr, sav

	def inList(self, find, arr):
		for a in arr:
			if a.getName() == find:
				return a

		return None



	def getNames(self, find, a):
		for k in a:
			if find.getName() == k.getName():
				return k
		return None


	def getNodes(self, keys):
		val = {}
		for a in keys:
			if a in self.expl:
				val[a] = None
			else:
				self.expl.append(a)
				val[a] = self.getNeighbors(a)
		return val




	def getNeighbors(self, key):
		n = []
		for a in list(self.nodes[key.getName()].getConnections()):
			if type(a) != type(1) and type(a) != type(chr(70)):
				n.append(Path2(a.getId(), key.getPath()))
			else:
				n.append(Path2(a, key.getPath()))


		return n


	def setNodes(self, nod):
		self.nodes = nod


	def addNode(self, key, nod):
		self.nodes[key] = nod
