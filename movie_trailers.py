import fresh_tomatoes
import media

# Data for all movies stored.

"""Movie data to be stored as follows.
   Parental rating is stored as a string, hence the quotes.
movie_name = media.Movie(
    "Movie Name", "friendly_movie_name (letters, numbers and underscores only)",
    "Youtube preview URL", "Parental rating)"
"""

rounders = media.Movie(
    "Rounders","rounders",
    "https://www.youtube.com/watch?v=-Qv4K-4-FZM","15")

fight_club = media.Movie(
    "Fight Club","fight_club",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg","18")

the_wolf_of_wall_street = media.Movie(
    "The Wolf of Wall Street","the_wolf_of_wall_street",
    "https://www.youtube.com/watch?v=iszwuX1AK6A","18")

the_shawshank_redemption= media.Movie(
    "The Shawshank Redemption","the_shawshank_redemption",
    "https://www.youtube.com/watch?v=6hB3S9bIaco","15")

the_dark_knight= media.Movie(
    "The Dark Knight","the_dark_knight",
    "https://www.youtube.com/watch?v=_PZpmTj1Q8Q","12A")

saving_private_ryan= media.Movie(
    "Saving Private Ryan","saving_private_ryan",
    "https://www.youtube.com/watch?v=zwhP5b4tD6g","15")

the_silence_of_the_lambs= media.Movie(
    "The Silence of the Lambs","the_silence_of_the_lambs",
    "https://www.youtube.com/watch?v=RuX2MQeb8UM","18")

star_wars_episode_iv_a_new_hope= media.Movie(
    "Star Wars: Episode IV - A New Hope","star_wars_episode_iv_a_new_hope",
    "https://www.youtube.com/watch?v=9gvqpFbRKtQ","U")

# Array of all movies to be displayed
movies = [saving_private_ryan,
          rounders,
          fight_club,
          star_wars_episode_iv_a_new_hope,
          the_wolf_of_wall_street,
          the_shawshank_redemption,
          the_dark_knight,
          the_silence_of_the_lambs]

# Calls open_movies_page function from fresh_tomates.py for all movies
# in the array.
# This generates fresh_tomatoes.html and then opens the page in the
# default webbrowser.

fresh_tomatoes.open_movies_page(movies)


