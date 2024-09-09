import numpy as np


def descison(x, w):
	return -w[0]+w[1]*x[0]+w[2]*x[1] >= 0


def error(w):
	cases = [
		descison([0, 0], w) != 0,
		descison([0, 1], w) != 0,
		descison([1, 0], w) != 0,
		descison([1, 1], w) != 0
	]
	return sum(cases)


results = dict()

for w1 in np.linspace(-6, 6, 100):
	for w2 in np.linspace(-6, 6, 100):
		w = np.array([1, w1, w2])
		results[(w1, w2)] = error(w)




print(min(results.items(), key=lambda x: x[1]))
print(max(results.items(), key=lambda x: x[1]))
