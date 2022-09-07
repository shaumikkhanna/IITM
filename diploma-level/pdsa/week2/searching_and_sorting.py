
def binary_search(l, v):
	"""Returns True if v is in l else False. """

	if not l:
		return False

	mid_index = len(l) // 2
	mid_value = l[mid_index]

	if v == mid_value:
		return True
	elif v < mid_value:
		return binary_search(l[:mid_index], v)
	else:
		return binary_search(l[mid_index+1:], v)


def selection_sort(l):
	"""Sorts a list using selection sort. """

	lst = l.copy()
	
	n = len(lst)

	if not n:
		return lst 

	for i in range(n):
		min_ind = i
		for j in range(i+1, n):
			if lst[j] < lst[min_ind]:
				min_ind = j

		lst[i], lst[min_ind] = lst[min_ind], lst[i]

	return lst


def insertion_sort(l):
	"""Sorts a list using insertion sort. """

	lst = l.copy()

	n = len(lst)

	if not n:
		return lst 

	for i in range(n):
		for j in range(i, 0, -1):
			if lst[j] < lst[j-1]:
				lst[j], lst[j-1] = lst[j-1], lst[j]
			else:
				break

	return lst


def insert(l, v):
	"""This function inserts a value v into a 
	sorted list l such that the final list is 
	also sorted. """

	n = len(l)

	if not n:
		return [v]

	if v >= l[-1]:
		return l + [v]
	else:
		return insert(l[:-1], v) + l[-1:]


def insertion_sort_recursive(l):
	"""Same as insertion_sort but this is recursive
	and expensive, may exceed Recursion limit. """

	n = len(l)

	if not n:
		return l 

	return insert(insertion_sort_recursive(l[:-1]), l[-1])


def merge(l1, l2):
	"""This function takes 2 sorted lists and then 
	merges them together into one sorted list. """

	if not l1:
		return l2
	if not l2:
		return l1

	out = []
	e1 = l1.pop(0)
	e2 = l2.pop(0)
	
	while True:
		
		if e1 < e2:
			out.append(e1)
			try:
				e1 = l1.pop(0)
			except IndexError:
				return out + [e2] + l2

		else:
			out.append(e2)
			try:
				e2 = l2.pop(0)
			except IndexError:
				return out + [e1] + l1


def merge_sort(l):
	"""Sorts a list using merge sort. """

	n = len(l)

	if n <= 1:
		return l

	L = merge_sort(l[:n//2])
	R = merge_sort(l[n//2:])

	return merge(L, R)

