"""
CP1404 Assignment 1 - Must-See Movies 1.0
Name: YOUR NAME
Date: 2025-06-20
Description: A program to manage watched and unwatched movies using a CSV file.
"""

FILENAME = "movies.csv"
WATCHED = 'w'
UNWATCHED = 'u'
VALID_CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]

def main():
    print("Must-See Movies 1.0 - by YOUR NAME")
    movies = load_movies(FILENAME)
    print(f"{len(movies)} movies loaded from {FILENAME}")
    menu = "dawq"
    choice = ""
    while choice != "q":
        print_menu()
        choice = input(">>> ").lower()
        if choice == "d":
            display_movies(movies)
        elif choice == "a":
            add_movie(movies)
        elif choice == "w":
            mark_movie_as_watched(movies)
        elif choice == "q":
            save_movies(FILENAME, movies)
            print(f"{len(movies)} movies saved to {FILENAME}")
            print("Have a nice day :)")
        else:
            print("Invalid menu choice")


def print_menu():
    print("Menu:")
    print("D - Display movies")
    print("A - Add new movie")
    print("W - Watch a movie")
    print("Q - Quit")


def load_movies(filename):
    movies = []
    with open(filename, 'r', encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            title = parts[0]
            year = int(parts[1])
            category = parts[2]
            status = parts[3]
            movies.append([title, year, category, status])
    return movies


def save_movies(filename, movies):
    with open(filename, 'w', encoding="utf-8") as out_file:
        for movie in movies:
            print(f"{movie[0]},{movie[1]},{movie[2]},{movie[3]}", file=out_file)


def display_movies(movies):
    movies.sort(key=lambda m: (m[1], m[0]))  # Sort by year, then title
    to_watch = 0
    watched = 0
    for i, movie in enumerate(movies, start=1):
        mark = "*" if movie[3] == UNWATCHED else " "
        print(f"{i}. {mark} {movie[0]:35} - {movie[1]} ({movie[2]})")
        if movie[3] == UNWATCHED:
            to_watch += 1
        else:
            watched += 1
    print(f"{watched} movies watched. {to_watch} movies still to watch.")


def add_movie(movies):
    title = get_non_empty_string("Title: ")
    year = get_valid_int("Year: ")
    print("Categories available:", ", ".join(VALID_CATEGORIES))
    category_input = input("Category: ").strip().capitalize()
    if category_input not in VALID_CATEGORIES:
        print("Invalid category; using Other")
        category_input = "Other"
    movies.append([title, year, category_input, UNWATCHED])
    print(f"{title} ({category_input} from {year}) added to movie list")


def mark_movie_as_watched(movies):
    unwatched_movies = [m for m in movies if m[3] == UNWATCHED]
    if not unwatched_movies:
        print("No more movies to watch!")
        return

    display_movies(movies)
    number = get_valid_int("Enter the movie number to mark watched.\n>>> ")
    if number < 1 or number > len(movies):
        print("Invalid movie number.")
    elif movies[number - 1][3] == WATCHED:
        print(f"You have already watched {movies[number - 1][0]}.")
    else:
        movies[number - 1][3] = WATCHED
        print(f"{movies[number - 1][0]} ({movies[number - 1][1]}) watched.")


def get_non_empty_string(prompt):
    value = input(prompt).strip()
    while value == "":
        print("Input can not be blank")
        value = input(prompt).strip()
    return value


def get_valid_int(prompt):
    number = None
    while number is None:
        user_input = input(prompt)
        if user_input.strip() == "":
            print("Invalid input; enter a valid number")
            continue
        try:
            value = int(user_input)
            if value < 1:
                print("Number must be >= 1")
            else:
                number = value
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


if __name__ == '__main__':
    main()
