from path import Path
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.lK = [key]

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def addNeighbors(self, nbr):
        self.connectedTo[nbr.getId()] = nbr

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()


    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def addPath(self, key):
        self.lK.append(key)

    def getLastKey(self):
        self.lK[len(self.lK) - 1]

