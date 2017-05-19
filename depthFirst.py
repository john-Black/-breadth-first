from path import Path
from stack import Stack

class DepthFirst:
    def __init__(self, ver = {}):
        self.expl = Stack()
        self.vertList = ver
    
    def run(self, first, last):
        self.expl.clear()
        return self.DfsIter(first, last)

    def addNode(self, key, nod):
        self.vertList[key] = nod


    def DfsIter(self, key, find):
        self.expl.push(key)

        n = Stack(self.getNeighbors(key))
        n.sort()

        if find in n:
            return Path(find, key)

        for a in n:
            if a in self.expl:
                continue
            else:
                curr = self.DfsIter(a, find)
                if curr != None:
                    curr.addPathVertex(key)
                    return curr
        return None

   
    
    def getNeighbors(self, key):
        n = []
        for a in list(self.vertList[key].getConnections()):
            if type(a) == type(1) or type(a) == type(chr(70)):
                n.append(a)
            else:
                n.append(a.getId())

        return n
        
