import networkx as nx
import matplotlib.pyplot as plt
from Post import Post
from User import User

def SocialMediaDiagram(listOfUsers):
    G = nx.DiGraph()
    digram = plt

    for user in listOfUsers:
        # Adds users as nodes
        G.add_node(user.userName)

        # Adds authored posts as nodes and creates edges between associated user
        for authoredPost in user.posts:
            G.add_node(authoredPost)
            G.add_edge(user, authoredPost, status='authored')
        
        # Adds viewed posts as nodes and creates edges between associated user
        for viewedPost in user.viewedPosts:
            G.add_node(viewedPost)
            G.add_edge(user, viewedPost, status='viewed')
        
    # Gets the weight of the edges for graphing
    edge_labels = nx.get_edge_attributes(G, 'status')

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()
        
