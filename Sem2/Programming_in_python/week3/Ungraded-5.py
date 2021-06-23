n = int(input())

answers = []
for z in range(1, n):
	for y in range(1, z):
		for x in range(1, y):
			if x**4 + y**3 == z**2:
				answers.append((x, y, z))

answers.sort(key=lambda x: x[0])
for answer in answers:
	print('{} {} {}'.format(*answer))

