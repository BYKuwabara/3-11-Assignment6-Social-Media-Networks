from collections import defaultdict

## This class will be used to represent connections between users

class DirectedWeightedGraph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def addEdge(self, u, v, weight):
        self.graph[u][v] = weight
    
    def getEdges(self):
        edges = []
        for u in self.graph:
            for v in self.graph:
                edges.append((u,v,self.graph[u][v]))
        return edges