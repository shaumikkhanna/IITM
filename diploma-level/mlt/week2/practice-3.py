import numpy as np


def loss(X, w, y):
	try:
		X = np.concatenate((
				np.ones(shape=(X.shape[0], 1)), X
			), axis=1)
		return 1/2 * np.linalg.norm(np.matmul(X, w) - y)**2
	except ValueError:
		pass
