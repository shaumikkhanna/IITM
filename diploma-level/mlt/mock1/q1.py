import numpy as np
import random

def loss(X, y, w, lr):
	X = np.concatenate((np.ones(shape=(X.shape[0], 1)), X), axis=1)
	sum_of_squares = 0.5*sum((X@w - y)**2)
	ridge_loss = lr/2*sum(w**2)
	lasso_loss = lr/2*sum(abs(c) for c in w)
	return sum_of_squares + min((ridge_loss, lasso_loss))
