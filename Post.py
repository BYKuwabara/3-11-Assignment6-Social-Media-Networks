class Post:
    def __init__(self, Content, Comments, Views, CreationDateAndTime):
        self.content = Content ## String
        self.comments = Comments ## Dictionary with comment as key and user as value
        self.views = Views ## List of usernames that viewed a post
        self.creationDateAndTime = CreationDateAndTime ## Creation date and time with the format of: month/day/year:time EX: 08/13/24:1340 => August 13 2024, 1:40 PM
