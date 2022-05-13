import numpy as np


def gradient(X, w, y):
	# Preprocessing of X
	X = np.concatenate((
			np.ones(shape=(X.shape[0], 1)), X
		), axis=1)

	if X.shape[-1] == w.shape[0]:
		return X.transpose() @ (X @ w - y)