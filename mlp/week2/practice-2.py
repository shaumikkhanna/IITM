import numpy as np


def multiply(X, w):
	if X.shape[1] + 1 == w.shape[0]:
		X = np.concatenate((
				np.ones(shape=(X.shape[0], 1)), X
			), axis=1)
		return np.matmul(X, w)
