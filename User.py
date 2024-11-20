class User:
    def __init__(self, UserName, Connections, Posts, PostedComments, ViewedPosts):
        self.userName = UserName
        self.connections = Connections # Will be represented using DirectedWeightedGraph class
        self.posts = Posts # Will be represented by a list of Posts
        self.postedComments = PostedComments # Will be represented by a list of strings
        self.viewedPosts = ViewedPosts # Will be represented by a list of Posts
        self.attributes = Attributes # Will be represented by a dictionary with attribute as key and value as value
