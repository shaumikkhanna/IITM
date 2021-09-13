my_list = input().split(' ')


for _ in range(int(input())):
	my_list = my_list[-1:] + my_list[:-1]

print(' '.join(my_list))