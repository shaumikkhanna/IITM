import numpy as np


def add_matrix(X, Y):
	if X.shape == Y.shape:
		return X+Y