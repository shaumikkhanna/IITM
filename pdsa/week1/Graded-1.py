
def find_Min_Difference(l, p):
	l.sort()
	min_ = l[-1]
	ind = 0

	while True:
		try:
			diff = l[ind + p - 1] - l[ind]
			if diff < min_:
				min_ = diff
			ind += 1
		except IndexError:
			return min_
