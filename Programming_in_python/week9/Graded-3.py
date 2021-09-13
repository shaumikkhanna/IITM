def solution():

	with open('version_1.txt', 'r') as f:
		version_1 = [line.strip() for line in f.readlines()]

	count = 0
	with open('version_2.txt', 'r') as f:
		for line in f.readlines():
			count += line.strip() not in version_1

	return count 
