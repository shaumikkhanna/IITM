def is_magic(mtx):
	n = len(mtx)
	magic_number = sum(mtx[0])

	# Row sums
	for row in mtx:
		if sum(row) != magic_number:
			return 'NO'

	# Column sums
	for ind in range(n):
		if sum(row[ind] for row in mtx) != magic_number:
			return 'NO'

	# Diagonal sums
	if sum(mtx[ind][ind] for ind in range(n)) != magic_number:
		return 'NO'
	if sum(mtx[ind][n-ind-1] for ind in range(n)) != magic_number:
		return 'NO'

	return 'YES'