n = int(input())

if n > 1:
	pattern = []
	block = (n - 3) // 2
	for i in range(block):
		my_string = ' '*i + '*' + ' '*(block-1-i)
		pattern.append('*' + my_string + '*' + my_string[::-1] + '*')
	print('*'*n)
	for p in pattern:
		print(p)
	print('*'*n)
	for p in pattern[::-1]:
		print(p)
	print('*'*n)
else:
	print('*')
