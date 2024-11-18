from collections import defaultdict

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