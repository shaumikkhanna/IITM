mtx = []
while True:
	input_ = input()
	if input_:
		mtx.append(input_.split(' '))
	else:
		break

for row in mtx:
	row.reverse()

for line in zip(*mtx):
	print(' '.join(line))