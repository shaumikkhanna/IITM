# One test case failed, I think it is an edge case of a lower 
# odd number like 3 or 1 but cannot figure out what the expected output is.

n = int(input())


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
