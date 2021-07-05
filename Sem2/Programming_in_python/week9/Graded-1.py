import pandas as pd 

def solution():

	# Read the file
	data = pd.read_csv('WorldPopulation.csv', header=0)

	year_query = int(input())
	print(data[data['Year'] == year_query]['Population'])

	population_query = int(input())
	print(min(data[data['Population'] > population_query]['Year']))

	max_query = input()
	print(max(data[max_query]))



