import networkx as nx
import matplotlib as plt
from Post import Post
from User import User

def SocialMediaDiagram(listOfUsers):
    G = nx.DiGraph()
    digram = plt.pyplot

    for user in listOfUsers:
        # Adds users as nodes
        G.add_node(user.userName)

        # Adds authored posts as nodes and creates edges between associated user
        for authoredPost in listOfUsers.posts:
            G.add_node(authoredPost)
            G.add_edge(user, authoredPost, 'authored')
        
        # Adds viewed posts as nodes and creates edges between associated user
        for viewedPost in listOfUsers.viewedPosts:
            G.add_edge(user, viewedPost, 'viewed')
        
        
