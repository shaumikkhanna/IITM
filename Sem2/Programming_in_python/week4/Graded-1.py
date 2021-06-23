data = []

while True:
	input_ = input()
	if input_ == 'END':
		break
	else:
		data.append(float(input_))

n = len(data)
mean = sum(data) / n 
squared_deviations = [(datapoint - mean)**2 for datapoint in data]
standard_deviation = (sum(squared_deviations)/(n-1))**.5

print(f'{standard_deviation:.2f}')