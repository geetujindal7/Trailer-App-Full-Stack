import webbrowser


#making movie class to define parts
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#function defination to open webbrowser
    def video(self):
        webbrowser.open(self.trailer_youtube_url)
