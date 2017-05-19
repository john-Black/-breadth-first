from graph import Graph


g = Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0,1,3)
g.addEdge(0,4,4)
g.addEdge(1,2,4)
g.addEdge(1,4,5)
g.addEdge(2,2,4)
g.addEdge(2,5,5)
g.addEdge(2,3,4)
g.addEdge(4,5,2)
g.addEdge(5,6,4)

g.addEdge(6,7,3)


for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))


print("Path Build\n")
fir = 0
las = 7
dsa = g.dfs(fir, las).getPath()
bsa = g.bfs(fir, las).getPath()
print("Depth First:", dsa)
print("Breadth First:", bsa)
