my_string = input().split(',')


my_list = []
for el in my_string:
	if el not in my_list:
		my_list.append(el)

print(','.join(my_list))