num = int(input())


divisor = 2
primes = []
ans = []

while divisor <= num:
	for prime in primes:
		if divisor % prime == 0:
			break
	else:
		primes.append(divisor)
		if num % divisor == 0:
			ans.append(divisor)

	divisor += 1

for x in ans:
	print(x)