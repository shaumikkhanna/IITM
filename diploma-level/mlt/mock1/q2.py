import numpy as np
import functools
import itertools


def polynomial_transform(x, degree):
	x = x.reshape((-1, 1))
	X = np.concatenate((
		np.ones(shape=x.shape), x, x**2
	), axis=1)
	return X

def output(x,y,test):
	X = polynomial_transform(x, 2)
	w = np.array([0, 0, 0])
	lr = 0.001
	for _ in range(300):
		for datapoint, label in zip(X, y):
			w = w - lr * (np.dot(datapoint, w) - label) * datapoint
	test = polynomial_transform(test, 2)
	print(w)
	return np.dot(test, w)
