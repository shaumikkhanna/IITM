my_string = input()


depth = 0
max_depth = depth

for letter in my_string:
	if letter == '(':
		depth += 1
	elif letter == ')':
		depth -= 1

	if depth < 0:
		print('Not matched')
		break

	max_depth = max([max_depth, depth])

else:
	print(max_depth)