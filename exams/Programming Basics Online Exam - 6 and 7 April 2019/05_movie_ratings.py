from sys import maxsize

n = int(input())
highest_rating = -maxsize
lowest_rating = maxsize
highest_rated_movie = ""
lowest_rated_movie = ""
total_rating = 0

for i in range(1, n+1):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating

    if movie_rating > highest_rating:
        highest_rating = movie_rating
        highest_rated_movie = movie_name
    
    if movie_rating < lowest_rating:
        lowest_rating = movie_rating
        lowest_rated_movie = movie_name

avg_rating = total_rating / n

print(f"{highest_rated_movie} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rated_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {avg_rating:.1f}")
