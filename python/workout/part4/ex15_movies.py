def movie_tracker():

    movies: dict[str, list[int]] = {}

    while True:
        title = input("Enter a movie title: ")

        if title == "":
            break

        rating = int(input("Enter a rating (1-10): "))

        movies.setdefault(title, []).append(rating)

    print("")
    print("Movie Rating Report:")

    for movie, ratings in movies.items():
        ratings_sum = sum(ratings)
        average = ratings_sum / len(ratings)

        print(f"{movie}: {average} average ({len(ratings)} ratings)")


if __name__ == "__main__":
    movie_tracker()
