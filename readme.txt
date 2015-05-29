###### Movie Trailers #####

### General overview

When the movie_trailers.py file is run it will generate
and open an html file for the movies stored.

When a movie poster image is hovered the border will turn
grey and the parental rating (based on the UK ratings)
will be displayed in the bottom right hand corner of
the post image.

When clicked the youtube trailer will be played.

### Files and folders:
movie_trailers.py
media.py
fresh_tomatoes.py
i/movie_poster/

## movie_trailers.py

This contains data for each movie, stored in the the
media.Movie class.

To add movies a new instance should be created using the
media.Movie class and then this should be added to the movies array. The poster image will also need to be added
to the folder "i/movie_poster" named as the "friendly_movie_name.jpg"

When run it will generate the fresh_tomatoes.html
in the same directory.


## media.py

This contains the Movie class and is used to create
an instance of each movie.

## fresh_tomatoes.py

This generates the html code to display all the movies.

## i/movie_poster/

This stores the movie post images. They must be stored
as their friendly_name with the filetype .jpg.