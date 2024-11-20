from datetime import datetime
#from collections import defaultdict

class TrendingPostAnalyzer:
    def __init__(self, users):
        self.users = users  # List of User objects

    def parse_datetime(self, datetime_str):
        return datetime.strptime(datetime_str, "%m/%d/%Y:%H%M")

    def trending_posts(
        self, 
        start_time, 
        end_time, 
        include_keywords=None, 
        exclude_keywords=None, 
        user_filters=None
    ):
        """
        Produces a report of trending posts based on multiple filters.

        param start_time: String, start time in the format "MM/DD/YYYY:HHMM".
        param end_time: String, end time in the format "MM/DD/YYYY:HHMM".
        param include_keywords: List of strings, include posts containing these keywords.
        param exclude_keywords: List of strings, exclude posts containing these keywords.
        param user_filters: Dictionary, filter posts by user attributes (e.g., {"age": 25}).
        return: List of tuples (Post, trend_rate), sorted by trend rate in descending order.
        
        """
        start_time = self.parse_datetime(start_time)
        end_time = self.parse_datetime(end_time)

        post_trend_data = []  # List of tuples (Post, trend_rate)

        for user in self.users:
            # Filter by user attributes
            if user_filters:
                if not all(user.attributes.get(k) == v for k, v in user_filters.items()):
                    continue

            for post in user.posts:
                # Filter by keywords (inclusion)
                if include_keywords and not any(word in post.content for word in include_keywords):
                    continue

                # Filter by keywords (exclusion)
                if exclude_keywords and any(word in post.content for word in exclude_keywords):
                    continue

                # Count views within the specified time range
                views_in_range = [
                    view_time for view_time in post.views
                    if start_time <= self.parse_datetime(view_time) <= end_time
                ]

                # Calculate trend rate
                trend_rate = len(views_in_range) / ((end_time - start_time).total_seconds() / 3600)
                post_trend_data.append((post, trend_rate))

        # Sort posts by trend rate in descending order
        post_trend_data.sort(key=lambda x: x[1], reverse=True)
        return post_trend_data
