import networkx as nx
from User import User
from Post import Post
from DirectedWeightedGraph import DirectedWeightedGraph
import matplotlib.pyplot as plt

def create_social_media_graph(users):
    G = nx.DiGraph()

    # Add user nodes
    for user in users:
        G.add_node(user.userName, label=user.userName, type='user', **user.attributes)

    # Add post nodes and edges
    for user in users:
        for post in user.posts:
            post_id = post.creationDateAndTime  # Unique identifier for the post
            G.add_node(post_id, label=post.content[:30] + "...", type='post', creationDate=post.creationDateAndTime)

            # Add edge for authorship
            G.add_edge(user.userName, post_id, type='author', relationship='author')

            # Add edges for comments
            for comment, commenter in post.comments.items():
                G.add_edge(commenter, post_id, type='comment', relationship=f'comment: "{comment}"')

            # Add edges for views
            for viewer in post.views:
                G.add_edge(viewer, post_id, type='view', relationship='viewed')

    return G

def highlight_interesting_users(G, criteria):
    interesting_users = []
    for node, data in G.nodes(data=True):
        if data['type'] == 'user' and all(criteria[key](data[key]) for key in criteria):
            interesting_users.append(node)
    return interesting_users

def draw_graph(G, interesting_users):
    pos = nx.spring_layout(G)
    node_colors = ['red' if node in interesting_users else 'blue' for node in G.nodes()]
    node_labels = nx.get_node_attributes(G, 'label')
    edge_labels = nx.get_edge_attributes(G, 'relationship')

    nx.draw(G, pos, node_color=node_colors, with_labels=True, labels=node_labels, node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.show()


