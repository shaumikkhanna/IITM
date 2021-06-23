# One test case failed, cannot seem to figure it out. Suspect a 
# problem with the grader or some kind of formattingerror.


n = int(input())


for z in range(1, n):
	for y in range(1, z):
		for x in range(1, y):
			if x**4 + y**3 == z**2:
				print(f'{x} {y} {z}')

