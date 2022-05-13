import numpy as np


def dot_product(u, v):
	if u.shape == v.shape:
		return np.dot(u, v)