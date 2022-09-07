import numpy as np


def percep_loss(x,w,y):
	loss = []
	for datapoint, label in zip(x, y):
		h = np.dot(datapoint, w)[0]
		y_hat = 1 if h > 0 else -1
		if label == y_hat:
			loss.append(0)
		else:
			loss.append(-label*h)

	print(loss)
	return loss