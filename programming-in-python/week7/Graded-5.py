def collatz(num):
	if not num % 2:
		return num // 2
	else:
		return 3 * num + 1

def collatz_repeat(n):
	count = 0
	while n != 1:
		n = collatz(n)
		count += 1
	return count