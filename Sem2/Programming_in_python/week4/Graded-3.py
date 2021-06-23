my_list = []

while True:
	input_ = input()
	if input_:
		my_list.append(int(input_))
	else:
		break

my_list = sorted(my_list)

out = []
for ind1 in range(len(my_list)):
	for ind2 in range(len(my_list)):
		if ind1 == ind2:
			continue

		x, y = my_list[ind1], my_list[ind2]
		if (x + y) in my_list:
			out.append((x, y))

print('\n'.join('{} {}'.format(*x) for x in out))