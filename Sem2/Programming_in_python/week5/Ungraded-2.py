def transpose(mtx):
	n = len(mtx[0])
	new_mtx = [[] for _ in range(n)]
	for col_no in range(n):
		new_row = []
		for row in mtx:
			new_row.append(row[col_no])
		new_mtx[col_no] = new_row

	return new_mtx