class User:
    def __init__(self, UserName, Connections, Posts):
        self.userName = UserName
        self.connections = Connections # Will be represented using DirectedWeightedGraph class
        self.posts = Posts # Will be represented using Posts class
