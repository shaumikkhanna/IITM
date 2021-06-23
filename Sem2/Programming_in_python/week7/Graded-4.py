M, N = int(input()), int(input())

# First row
print(input())

# Middle rows
for _ in range(M-2):
	first, *_, last = input().split()
	row = [first] + ['0' for _ in range(N-2)] + [last]
	print(' '.join(row))

# Last row
print(input())