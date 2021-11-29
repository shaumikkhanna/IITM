import numpy as np
import math


def eta(t):
	return 0.1

def grad_f(*x):
	return np.array([
		math.sin(x[0]) + x[0]*math.cos(x[0])
		])

def iterme(start, step_size, gradient, times):
	value = start
	for t in range(times):
		value -= step_size(t)*gradient(value)
	return value


print(iterme(np.array([2.5]), eta, grad_f, 4))
