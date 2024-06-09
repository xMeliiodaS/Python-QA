import datetime


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


def add_movie_dynamic_rating(movie_list: list, movie_ratings: dict) -> None:
    """
    Adding a movie to the list also updates the movie_ratings dictionary
    """
    new_movie = input("Enter movie name to add to the movie list: ")
    movie_list.append(new_movie)
    movie_ratings[new_movie] = 5


def add_movies_until_exit(movie_list: list, movie_ratings: dict, stop_condition: str) -> None:
    """
    Adding movies to the movie list until the condition is not met
    :param movie_list: List of movies
    """
    while True:
        new_movie = input(f"Enter movie name to the list: (Stop by typing: {stop_condition})")
        if stop_condition != new_movie:
            movie_list.append(new_movie)
            movie_ratings[new_movie] = 5
            write_log_file(new_movie)
        else:
            print()
            read_log_file()
            break


def write_log_file(movie_name) -> None:
    try:
        with open('Time_log.txt', 'a') as file:
            current_time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            file.write(f"{current_time} - {movie_name} was added to the dictionary.\n")
    except FileNotFoundError:
        print("File not found")


def read_log_file() -> None:
    try:
        with open('Time_log.txt', 'r') as file:
            content = file.read()
            print(f'All movies that got added to dictionary by input:\n{content}')
    except FileNotFoundError:
        print("File not found")


# 1 - List of movies
movie_list = ["Harry Potter", "Wednesday", "AOT", "Breaking bad", "Re:zero"]
print_movie_list(movie_list)

add_movie(movie_list, "Dark")
print_movie_list(movie_list)

# 2 - Set of actors
actor_set = {"Harry", "Eren", "Meliiodas"}
print_movie_list(actor_set)

add_actor(actor_set, "Eren")
print_movie_list(actor_set)

# 3 - Dictionary of movie ratings
movie_ratings = {"Harry Potter": 7, "Wednesday": 9, "AOT": 9.8, "Breaking bad": 8.4, "Re:zero": 9.1}
print_movie_ratings(movie_ratings)

# Dictionary with movies and their actors
movies_with_actors = {"Harry Potter": ["Harry", "Bata", "Sambosek"],
                      "Wednesday": ["Idk", "Didn't", "Watch", "It"],
                      "AOT": ["Eren", "Mikasa", "Armin", "Levi"],
                      "Breaking bad": ["This", "Onw", "Too", "xD"],
                      "Re:zero": ["Subaru", "Rem", "Rom"]}

# add_movie_dynamic_rating(movie_list, movie_ratings)
# print(movie_list)
# print(movie_ratings)

add_movies_until_exit(movie_list, movie_ratings, "stop")
print(movie_list)
print(movie_ratings)
