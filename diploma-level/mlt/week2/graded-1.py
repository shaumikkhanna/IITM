import numpy as np


def compatibility(X, w):
	if X.shape[-1] != w.shape[0]:
		return 'C'
