from collections import namedtuple, defaultdict, Counter
import csv
import random
from urllib.request import urlretrieve
from datetime import datetime, date, timedelta


movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movie.csv'
urlretrieve(movie_data, movies_csv)

Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data = movies_csv):
	"""Extracts all movies from csv and stores them in dictionary
		where keys are directors, and values is a list of movies
	"""
	directors = defaultdict(list)
	with open(data, encoding='utf-8') as f:
		for line in csv.DictReader(f):
			try:
				director = line['director_name']
				movie = line['movie_title'].replace('\xa0','')
				year = int(line['title_year'])
				score = float(line['imdb_score'])
			except ValueError:
				continue
			m = Movie(title = movie, year = year, score = score)
			directors[director].append(m)
	
	return directors

directors = get_movies_by_director()

print(directors['Christopher Nolan'])


cnt = Counter()

for director, movie in directors.items():
	cnt[director] += len(movie)

print(cnt.most_common(10))



#TODO: Try pybites challenge: https://pybit.es/codechallenge13.html
