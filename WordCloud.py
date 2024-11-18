from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from collections import defaultdict
from Post import Post
from User import User

class SocialMediaWordCloud:
    def __init__(self, users):
        # List of User objects
        self.users = users 

    def generate_word_cloud(self, include_keywords=None, exclude_keywords=None, user_filters=None):
        # Filter users based on user_filters
        filtered_users = self.users
        if user_filters:
            for key, value in user_filters.items():
                filtered_users = [user for user in filtered_users if getattr(user, key, None) == value]

        # Collect posts based on include/exclude keywords
        text_collection = []
        for user in filtered_users:
            for post in user.posts:
                # Apply include keywords filter
                if include_keywords and not any(keyword in post.content for keyword in include_keywords):
                    continue
                # Apply exclude keywords filter
                if exclude_keywords and any(keyword in post.content for keyword in exclude_keywords):
                    continue
                # Add post content to the text collection
                text_collection.append(post.content)

        # Combine all filtered text into a single string
        combined_text = " ".join(text_collection)

        # Create and return the WordCloud object
        stopwords = set(STOPWORDS)
        wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=800, height=400).generate(combined_text)
        return wordcloud

    @staticmethod
    def display_word_cloud(wordcloud):
        # Display the WordCloud object
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
