def perfect_number(num):
	total = 0
	for divisor in range(1, num):
		if not num % divisor:
			total += divisor

	return total == num