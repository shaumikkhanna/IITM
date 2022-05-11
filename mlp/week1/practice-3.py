import numpy as np


def hadamard(u, v):
	try:
		return u*v
	except ValueError:
		pass