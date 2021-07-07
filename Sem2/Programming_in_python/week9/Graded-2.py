def highest_grossing(year_from, year_upto, genre):

	# Reading data
	data = []
	with open('IMDB_reviews.csv', 'r') as f:
		column_names = f.readline().strip().split(',')
		for line in f.readlines():
			datapoint = line.strip().split(',')
			data.append(dict(zip(column_names, datapoint)))

	highest_grossing_movie = None
	highest_gross = 0
	for movie in data:
		year_of_release = int(movie['year'])
		if (year_from <= year_of_release <= year_upto) and genre in movie['genre']:
			try:
				gross = int(movie['gross'])
			except ValueError:
				continue
			if gross > highest_gross:
				highest_gross = gross
				highest_grossing_movie = movie['name']

	return highest_grossing_movie
