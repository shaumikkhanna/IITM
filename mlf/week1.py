import numpy as np


def dimensionality_reduction_loss(encoder, decoder, data):
	n = len(data)
	deviations = np.array([decoder(encoder(datapoint)) - datapoint for datapoint in data])
	return 1 / n * sum(sum(deviation**2) for deviation in deviations)


def mean_squared_error_loss(f, data, labels):
	n = len(data)
	return 1 /n * sum((f(datapoint) - label)**2 for datapoint, label in zip(data, labels))


def linear_function(*coefficients):
	*a, b = coefficients
	def inner_func(point):
		return sum(a0*p0 for a0, p0 in zip(a, point)) + b
	return inner_func


def sign(num):
	if num >= 0:
		return 1
	else:
		return -1


def misclassification_loss(f, data, labels):
	n = len(data)
	return 1 / n * sum(sign(f(datapoint)) != label for datapoint, label in zip(data, labels))


###
print('q11, 12')

data = np.array([
	[1, 0.5],
	[2, 2.3],
	[3, 3.1],
	[4, 3.9]
	])

def f1(point):
	return (point[0] - point[1], )

def g(point):
	return (point[0]/2, point[0]/2)

def f2(point):
	return ((point[0] + point[1])/2, )

print(dimensionality_reduction_loss(f1, g, data))
print(dimensionality_reduction_loss(f2, g, data))
print()


###
print('q13')

data = np.array([
	[-1],
	[0],
	[1],
	[2]
	])

labels = np.array([0.0319, 0.8692, 1.9566, 3.0343])

for a, b in [(1, 1), (1, 2), (2, 1), (2, 2)]:
	print(mean_squared_error_loss(linear_function(a, b), data, labels))

print()


###
print('q14, 15')

data = np.array([
	[2], 
	[3], 
	[6], 
	[7], 
	[8]
	])

labels = np.array([5.8, 8.3, 18.3, 21, 22])

print(mean_squared_error_loss(linear_function(3, 1), data, labels))
print(mean_squared_error_loss(linear_function(2, 2), data, labels))
print()


###
print('q16, 17')

data = np.array([
	[4, 2],
	[8, 4],
	[2, 6],
	[4, 10],
	[10, 2],
	[12, 8]
	])

labels = np.array([1, 1, -1, -1, 1, -1])

print(misclassification_loss(linear_function(1, -1, -2), data, labels))
print(misclassification_loss(linear_function(1, 1, -10), data, labels))
print()


###
print('q18')

data = np.array([
	[1, 2, 3],
	[2, 3, 4],
	[-1, 0, 1],
	[0, 1, 1]
	])

def f(point):
	return ((point[0] + 2*point[1])/2, )

def g(point):
	return (point[0], 2*point[0], 3*point[0])

print(dimensionality_reduction_loss(f, g, data))
print()

