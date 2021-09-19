
def process_line(i):
	with open('numbers.txt', 'r') as f:
		for _ in range(i):
			f.readline()
		line = f.readline().strip()

	try:
		numbers = [int(num) for num in line.split(',')]
	except ValueError:
		return -1, -1, -1

	N = len(numbers)
	S = sum(numbers)

	P = 1
	for num in numbers:
		P *= num 

	return N, S, P