import networkx as nx
import matplotlib.pyplot as plt

def SocialMediaDiagram(listOfUsers, importance_criteria='views'):
    G = nx.DiGraph()

    # Create nodes for users and posts, and edges between them
    for user in listOfUsers:
        G.add_node(user.userName)

        # Adding posts as nodes and connecting them with appropriate edges
        for post in user.posts:
            post_node_label = post.content[:15] + '...' if len(post.content) > 15 else post.content
            G.add_node(post_node_label)
            G.add_edge(user.userName, post_node_label, status='authored')
        
        for viewed_post in user.viewedPosts:
            viewed_post_label = viewed_post.content[:15] + '...' if len(viewed_post.content) > 15 else viewed_post.content
            G.add_node(viewed_post_label)
            G.add_edge(user.userName, viewed_post_label, status='viewed')

    # Calculate importance of posts and determine the one with the highest importance
    max_importance = -1
    post_with_max_importance = None
    node_colors = []
    node_sizes = []

    for node in G.nodes:
        # Skip user nodes and check only post nodes
        if node not in [user.userName for user in listOfUsers]:
            # Find the post associated with this node label
            post = next((p for user in listOfUsers for p in user.posts + user.viewedPosts if p.content.startswith(node[:-3])), None)
            
            if post:
                # Calculate importance based on views, comments, or both
                if importance_criteria == 'views':
                    importance = len(post.views)
                elif importance_criteria == 'comments':
                    importance = len(post.comments)
                elif importance_criteria == 'blend':
                    importance = len(post.views) + len(post.comments)
                else:
                    importance = 0  # Default if no valid criteria are specified

                # Keep track of the post with the highest importance
                if importance > max_importance:
                    max_importance = importance
                    post_with_max_importance = node
                
                # Default coloring and sizing for posts
                node_colors.append('lightblue')
                node_sizes.append(100)
            else:
                node_colors.append('lightblue')
                node_sizes.append(100)
        else:
            node_colors.append('lightgreen')  # User nodes color
            node_sizes.append(200)

    # Highlight the post with the maximum importance
    for i, node in enumerate(G.nodes):
        if node == post_with_max_importance:
            node_colors[i] = 'red'  # Highlight color for the most important post
            node_sizes[i] = 300 + max_importance * 20  # Scaled size for the most important post

    pos = nx.spring_layout(G, k=1.5, iterations=100)  # Adjust layout for better spacing
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes, font_size=10, font_weight='bold')

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'status')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()
