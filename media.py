import webbrowser
class Movie():
    """This class models a movie"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    __name__ = "Movie"
    __module__ = "media"
    
    def __init__(self, title, story, image, trailer):
        self.title = title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url, 0)
        
