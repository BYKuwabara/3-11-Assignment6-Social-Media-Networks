def main():
    from Post import Post
    from User import User
    from DirectedWeightedGraph import DirectedWeightedGraph
    from WordCloud import SocialMediaWordCloud
    from TrendingPosts import TrendingPostAnalyzer

     # Create Post objects with sample data
    post1 = Post(
        "First post content!", 
        {"Great post!": "Bob", "I love this!": "Charlie"},  # Bob and Charlie commented
        ["Bob", "Charlie"],  # Bob and Charlie viewed the post
        "11/10/24:0900"
    )
    post2 = Post(
        "Learning Python is fun!", 
        {"Python is awesome!": "Alice"},  # Alice commented
        ["Alice", "Bob"],  # Alice and Bob viewed the post
        "11/12/24:1015"
    )
    post3 = Post(
        "Just finished a great book!", 
        {"Nice book recommendation!": "David"},  # David commented
        ["David", "Alice"],  # Charlie and Alice viewed the post
        "11/14/24:1530"
    )

    # Create users and their corresponding connection graphs
    user1_connections = DirectedWeightedGraph()
    user1_connections.addEdge("Alice", "Bob", "friends")
    user1_connections.addEdge("Alice", "Charlie", "coworker")
    user1_connections.addEdge("Alice", "David", "has read posts by")  

    user2_connections = DirectedWeightedGraph()
    user2_connections.addEdge("Bob", "Alice", "friends")
    user2_connections.addEdge("Bob", "Charlie", "coworker")
    user2_connections.addEdge("Bob", "David", "has read posts by")  

    user3_connections = DirectedWeightedGraph()
    user3_connections.addEdge("Charlie", "Alice", "follows")
    user3_connections.addEdge("Charlie", "Bob", "blocked")
    user3_connections.addEdge("Charlie", "David", "has read posts by")  

    user4_connections = DirectedWeightedGraph()
    user4_connections.addEdge("David", "Alice", "has read posts by")  

    # Create User objects with their respective posts, comments, and connections
    user1 = User(
        "Alice", user1_connections, [post1, post2], 
        ["Nice post!", "Python is awesome!"], [post3]  
    )
    user2 = User(
        "Bob", user2_connections, [post3], 
        ["Great post!"], [post1, post2]  
    )
    user3 = User(
        "Charlie", user3_connections, [], 
        ["I love this!"], [post1]  
    )
    user4 = User(
        "David", user4_connections, [], 
        ["Nice book recommendation!"], []  
    )

    # Display user information
    users = [user1, user2, user3, user4]
    
    for user in users:
        print(f"User: {user.userName}")
        
        # Print posts
        print("  Posts:")
        for post in user.posts:
            print(f"    - {post.content} created on {post.creationDateAndTime}")
            print("      Comments:")
            for comment, comment_user in post.comments.items():
                print(f"        '{comment}' by {comment_user}")
            print(f"      Views: {', '.join(post.views)}")
        
        # Print connections
        print("  Connections:")
        for edge in user.connections.getEdges():
            print(f"    {edge[0]} -> {edge[1]} (Weight: {edge[2]})")

        print("  Posted Comments:")
        for comment in user.postedComments:
            print(f"    - {comment}")
        
        print()  # Blank line between users

    # Create a SocialMediaWordCloud object
    word_cloud_generator = SocialMediaWordCloud([user1, user2])
    wordcloud = word_cloud_generator.generate_word_cloud(include_keywords=["Python"])
    print("Displaying word cloud for posts containing 'Python':")
    word_cloud_generator.display_word_cloud(wordcloud)

     # Create a TrendingPostAnalyzer object and display trending posts
    # Example posts
    post1 = Post(
        "Post about AI",
        {"Interesting comment": "user1"},
        ["08/13/24:1345", "08/13/24:1400", "08/13/24:1415"],
        "08/13/24:1340",
    )
    post2 = Post(
        "Post about ML",
        {"Another comment": "user2"},
        ["08/13/24:1350", "08/13/24:1410"],
        "08/13/24:1330",
    )

    # Example users
    user1 = User("user1", [], [post1], [], [])
    user2 = User("user2", [], [post2], [], [])

    analyzer = TrendingPostAnalyzer([user1, user2])
    trending = analyzer.trending_posts("08/13/24:1330", "08/13/24:1430")
    for post, rate in trending:
        print(f"Post: {post.content}, Trend Rate: {rate}")

if __name__ == "__main__":
    main()