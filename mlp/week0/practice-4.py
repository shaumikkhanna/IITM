import numpy as np


def predict(w, x):
	return 1 if np.dot(w, x) >= 0 else -1