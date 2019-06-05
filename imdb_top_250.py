import imdb
import csv
import json

ia = imdb.IMDb()
top250 = ia.get_top250_movies()

# attrs = vars(ia)
# print(', '.join("%s: %s" % item for item in attrs.items()))

# test = top250[0]
# attrs = vars(test)
# print(', '.join("%s: %s" % item for item in attrs.items()))
# print(test)
# print(test.movieID)
# print(test.data)
# print(test.data['rating'])

movie_id = []
rating = []
title = []
year = []
votes = []
rank = []

for movie in top250:
    movie_id.append(movie.movieID)
    data = movie.data
    rating.append(data['rating'])
    title.append(data['title'])
    year.append(data['year'])
    votes.append(data['votes'])
    rank.append(data['top 250 rank'])


# print(movie_id[0], rating[0], title[0], year[0], votes[0], rank[0])
