
def mergeInPlace(a, b):
	for ind in range(len(a)):
		if a[ind] > b[0]:
			a.swap(ind, b, 0)
			sorted_insert(b)

def sorted_insert(l):
	n = len(l)
	for ind in range(n-1):
		if l[ind] > l[ind+1]:
			l.swap(ind, l, ind+1)
		else:
			break
	

## For testing

class mlist(list):
	def swap(self, indexA, other, indexB):
		self[indexA], other[indexB] = other[indexB], self[indexA]


