import numpy as np


def weight_update(X, w, y, lr):
	# Preprocessing of X
	X = np.concatenate((
			np.ones(shape=(X.shape[0], 1)), X
		), axis=1)

	# Gradient calculation
	if X.shape[-1] == w.shape[0]:
		g = X.transpose() @ (X @ w - y)
	else:
		return

	# Update weight
	w -= lr * g
	return w
