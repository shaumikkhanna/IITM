my_string = input()


primes = []
for divisor in range(2, len(my_string)):
	for prime in primes:
		if not divisor % prime:
			break
	else:
		primes.append(divisor)

for ind in primes:
	print(my_string[ind])