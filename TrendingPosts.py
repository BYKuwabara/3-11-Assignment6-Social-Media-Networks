from datetime import datetime
#from collections import defaultdict

class TrendingPostAnalyzer:
    def __init__(self, users):
        self.users = users  # List of User objects

    def parse_datetime(self, datetime_str):
        return datetime.strptime(datetime_str, "%m/%d/%Y:%H%M")

    def trending_posts(self, start_time, end_time):

        """
        Identifies trending posts based on the rate of new views.

        param start_time: String, start time in the format "MM/DD/YYYY:HHMM"
        param end_time: String, end time in the format "MM/DD/YYYY:HHMM"
        return: List of tuples (Post, trend_rate), sorted by trend_rate in descending order
        """
        start_time = self.parse_datetime(start_time)
        end_time = self.parse_datetime(end_time)

        # Step 1: Collect view counts for posts within the time range
        post_trend_data = []  # List of tuples (Post, trend_rate)
        for user in self.users:
            for post in user.posts:
                # Count views within the time range
                views_in_range = [
                    view_time for view_time in post.views
                    if start_time <= self.parse_datetime(view_time) <= end_time
                ]
                trend_rate = len(views_in_range) / ((end_time - start_time).total_seconds() / 3600)
                post_trend_data.append((post, trend_rate))

        # Step 2: Sort posts by their trend rate
        post_trend_data.sort(key=lambda x: x[1], reverse=True)
        return post_trend_data