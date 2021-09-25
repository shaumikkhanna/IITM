
def sortInRange(l, r):
	tally = [0 for _ in range(r)]
	while l:
		tally[l.pop()] += 1

	for k in range(r):
		l.extend([k for _ in range(tally[k])])

