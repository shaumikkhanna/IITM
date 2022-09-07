
def findLargest(l):
	first = l[0]
	last = l[-1]

	if first <= last:
		return last

	while len(l) > 1:
		mid_index = len(l) // 2
		mid_value = l[mid_index]

		if mid_value <= last:
			del l[mid_index:]
		else:
			del l[:mid_index]

	return l[0]

