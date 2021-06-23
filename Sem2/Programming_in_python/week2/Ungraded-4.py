my_string = input()


if len(my_string) % 2 == 0:
	if my_string[-1] == '.':
		my_string = my_string[:-1]
	else:
		my_string += '.'

ind = len(my_string) // 2
print(my_string[ind-1:ind+2])