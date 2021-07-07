def solution():

	# Read the file
	data = []
	with open('WorldPopulation.csv', 'r') as f:
		column_names = f.readline().strip().split(',')
		for line in f.readlines():
			datapoint = [float(x) for x in line.strip().split(',')]
			data.append(dict(zip(column_names, datapoint)))

	# First Query
	year_query = int(input())
	for datapoint in data:
		if datapoint['Year'] == year_query:
			print(int(datapoint['Population']))
			break

	# Second Query
	population_query = int(input())
	years_with_higher_pop = []
	for datapoint in data:
		if datapoint['Population'] > population_query:
			years_with_higher_pop.append(datapoint['Year'])
	print(int(min(years_with_higher_pop)))

	# Third Query
	field_query = input()
	print(max(data, key=lambda x: x[field_query])[field_query])

