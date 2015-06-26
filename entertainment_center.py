import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "The story of a boy's toys coming to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=RmFbmlwWa0k")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=eUTtt14G31c")

inception = media.Movie("Inception",
                        "A dream within a dream within a dream.",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=8BfMivMDOBI")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time love story.",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=5nOF93SzX6s")

movies = [toy_story, avatar, inception, midnight_in_paris]

fresh_tomatoes.open_movies_page(movies)

