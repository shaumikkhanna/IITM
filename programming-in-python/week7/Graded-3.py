def merge(D1, D2, priority):
	if priority == 'first':
		new = D2.copy()
		new.update(D1)
	else:
		new = D1.copy()
		new.update(D2)
	return new