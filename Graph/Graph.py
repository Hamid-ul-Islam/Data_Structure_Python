#graph implementation with adjMatrix (2d array) (initialized all matrix with 0) here nodes = vertices and node = vertex
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjMatrix = [[0] * vertices] * vertices #short form of listcomprehension [[0 for i in range(vertices)] for j in range(vertices)]
        
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
    def removeEdge(self):
    def hasEdge(self)