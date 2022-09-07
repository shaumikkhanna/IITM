import numpy as np


def IsNegativeWeightCyclePresent(wlist):
	n = len(wlist.keys())
	infinity = np.inf

	sp = np.zeros(shape=(n+1, n, n))
	for i in range(n):
		for j in range(n):
			sp[0, i, j] = infinity

	for u in wlist.keys():
		for v, d in wlist[u]:
			sp[0, u, v] = d

	for k in range(n):
		for i in range(n):
			for j in range(n):
				sp[k + 1, i, j] = min([
					sp[k, i, j],
					sp[k, i, k] + sp[k, k, j]
					])

	final = sp[-1, :, :]
	return any(final[i, i] < 0 for i in range(n))


# For testing

WL = {0: [(1, -10)], 1: [(2, -20)], 2: [(3, -20)], 3: []}
    
print(WL)
print(IsNegativeWeightCyclePresent(WL))


