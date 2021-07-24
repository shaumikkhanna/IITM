mtx = []
for _ in range(int(input())):
	mtx.append(input().split(','))

if input() == 'row': # Row reversing
	mtx.reverse()
else: # Column reversing
	for row in mtx:
		row.reverse()

for row in mtx:
	print(','.join(row))
