from collections import defaultdict

# This class will be used to represent connections between users

class DirectedWeightedGraph:
    def __init__(self):
        self.graph = defaultdict(dict)

    # Weight will be a string with a value of 'follows', 'friends', 'coworker', 'blocked', or 'has read posts by'.
    def addEdge(self, u, v, weight):
        self.graph[u][v] = weight
    
    def getEdges(self):
        edges = []
        for u in self.graph:
            for v in self.graph:
                edges.append((u,v,self.graph[u][v]))
        return edges
    # O(u * v) or O(n^2)