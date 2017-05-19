from vertex import Vertex
from path import Path
from depthFirst import DepthFirst
from breadthFirst import BreadthFirst

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.expl = []
        self.dFs = DepthFirst()
        self.bFs = BreadthFirst()



    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.dFs.addNode(key, newVertex)
        self.bFs.addNode(key, newVertex)
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


    def dfs(self, first, last):
        return self.dFs.run(first, last)


    def bfs(self, first, last):
        a, b = self.bFs.run(first, last)
        return b

    def getNeighbors(self, key):
        n = []
        for a in list(self.vertList[key].getConnections()):
            n.append(a.getId())

        return n
    
    

    def getTree(self, gr):
        for a in gr:
            print(a, self.getNeighbors(a))
