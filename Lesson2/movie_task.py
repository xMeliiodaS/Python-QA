def print_movie_list(movie_list: list) -> None:
    """
    Prints the list of movies
    :param movie_list: List of movies
    """
    print(movie_list)


def add_movie(movie_list: list, movie: str) -> None:
    """
    Adds a movie to the movie list and prints the updated list
    :param movie_list: list of movies
    :param movie: Movie to add
    """
    movie_list.append(movie)
    print(movie_list)
    print()


def print_actors_set(actors_set: set) -> None:
    """
    Prints the set of actors
    :param actors_set: Set of actors
    """
    print(actors_set)


def add_actor(actors_set: set, actor: str) -> None:
    """
    Adds an actor to the actors set and prints the updated set
    :param actors_set: Set of actors
    :param actor: Actor to add
    """
    actors_set.add(actor)
    print(actors_set)
    print()


def print_movie_ratings(movie_ratings: dict) -> None:
    """
    Prints the dictionary of movie ratings
    :param movie_ratings: Dictionary of movie ratings
    """
    print(movie_ratings)


# List of movies
movies = ["Harry Potter", "Wednesday", "AOT", "Breaking bad"]
print_movie_list(movies)

add_movie(movies, "Dark")

# Set of actors
actors = {"Harry", "Eren", "Meliodas"}
print_movie_list(actors)

add_actor(actors, "Eren")

# Dictionary of movie ratings
ratings = {"Harry Potter": 7, "Wednesday": 9, "AOT": 9.8, "Breaking bad": 8.4}
print_movie_ratings(ratings)

# Dictionary with movies and their actors
movie_with_actors = {"AOT": ["Eren", "Mikasa", "Armin", "Levi"],
                     "RE:ZERO": ["Subaru", "Rem", "Ram"],
                     "Demon Slayer": ["Tanjirou", "Nezoku", "Ma7mod"]}
