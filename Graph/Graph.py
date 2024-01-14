#graph implementation with adjMatrix (2d array) (initialized all matrix with 0) here nodes = vertices and node = vertex
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjMatrix = [[0 for i in range(vertices)] for j in range(vertices)] #short form of listcomprehension [[0 for i in range(vertices)] for j in range(vertices)]
        print(self.adjMatrix)
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v2] = 1

    def removeEdge(self, v1, v2):
        if self.hasEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v2] = 0
        
    def hasEdge(self, v1, v2):
        return self.adjMatrix[v1][v2] > 0
    
    #printing function
    def __str__(self) -> str:
        return str(self.adjMatrix)

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(1, 3)
g.addEdge(2, 4)

print(g)