def add_movie_to_boxoffice(movies_db, new_movie):
	name, collection, year = new_movie
	movies_db[name] = [collection, year]
	return movies_db

def total_collection(movies_db):
	return sum(collection for collection, *_ in movies_db.values())

def average_collection(movies_db):
	return round(total_collection(movies_db) / len(movies_db), 2)

def num_of_movies_above_average_movies(movies_db):
	avg = average_collection(movies_db)
	return sum(collection > avg for collection, *_ in movies_db.values())

def highest_grossing_movie_year(movies_db):
	return movies_db[max(movies_db, key=movies_db.get)][1]
