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
            G.add_edge(user, authoredPost, status='authored')
        
        # Adds viewed posts as nodes and creates edges between associated user
        for viewedPost in listOfUsers.viewedPosts:
            G.add_node(viewedPost)
            G.add_edge(user, viewedPost, status='viewed')
        
    # Gets the weight of the edges for graphing
    edge_weights = nx.get_edge_attributes(G, 'status')

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights)

    plt.show()
        
