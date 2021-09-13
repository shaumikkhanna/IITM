
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

def Goldbach(n):
	primes = prime_list(n)
	out = []

	for prime in primes:
		if prime > n / 2:
			break

		if n - prime in primes:
			out.append((prime, n - prime))

	return out

print(Goldbach(26))