import numpy as np


def add_one(X):
	return np.concatenate((
			np.ones(shape=(X.shape[0], 1)), X
		), axis=1)
	