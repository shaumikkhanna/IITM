n = int(input())


primes = []
for num in range(2, n+1):
	for prime in primes:
		if not num % prime:
			break
	else:
		primes.append(num)

print(sum(primes))