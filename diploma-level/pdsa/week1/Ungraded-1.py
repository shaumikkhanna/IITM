
def prime_list(m):
	"""Returns a list of odd primes less than m (inclusive)"""
	primes = []
	for i in range(3, m + 1, 2):
		for prime in primes:
			if i % prime == 0:
				break
		else:
			primes.append(i)

	return primes


def Twin_Primes(n, m):
	primes = [i for i in prime_list(m) if i >= n]
	out = []
	for a, b in zip([0] + primes, primes + [0]):
		if a + 2 == b:
			out.append((a, b))

	return out
