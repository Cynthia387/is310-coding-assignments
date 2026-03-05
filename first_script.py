favorite_movies = {
    "The Dark Knight": 2008,
    "Titanic": 1997,
    "Inception": 2010,
    "The Matrix": 1999,
    "Interstellar": 2014
}

def check_movie(movie):
    year = favorite_movies[movie]

    if year < 2000:
        print(movie + ": This movie was released before 2000")
    else:
        print(movie + ": This movie was released after 2000")
        return movie

recent_movies = []

for movie in favorite_movies:
    result = check_movie(movie)

    if result is not None:
        recent_movies.append(result)

print("Movies released after 2000:")
print(recent_movies)