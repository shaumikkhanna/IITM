
def combinationSort(lst):
	l1, l2 = [], []

	for el in lst:
		a, b = el[0], int(el[1:])

		# insert in l1
		for ind in range(len(l1)):
			if a < l1[ind][0]:
				l1.insert(ind, el)
				break
		else:
			l1.append(el)
		

		# insert in l2
		for ind in range(len(l2)):
			if a < l2[ind][0] or (a == l2[ind][0] and b > int(l2[ind][1:])):
				l2.insert(ind, el)
				break
		else:
			l2.append(el)

	return l1, l2

