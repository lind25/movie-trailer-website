class Movie():

    # Enables movie related information to be stored
    def __init__(self,
                 movie_title,
                 friendly_name,
                 movie_trailer,
                 movie_parental_rating):
        self.title=movie_title
        self.trailer_youtube_url=movie_trailer
        self.parental_rating=movie_parental_rating
        # set poster image URL based on movie name
        self.poster_image_url= "i/movie_poster/" + friendly_name + ".jpg"
