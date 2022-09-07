## Not finished

def binarySearchIndexAndComparisons(l, v, left=None, right=None, count=0):
	if left is None:
		left = 0
	if right is None:
		right = len(l) - 1

	if left == right:
		return False, count + 1

	mid_index = (left + right) // 2
	mid_value = l[mid_index]

	if v == mid_value:
		return True, count
	elif v < mid_value:
		return binarySearchIndexAndComparisons(l, v, left, mid_index - 1, count+1)
	else:
		return binarySearchIndexAndComparisons(l, v, mid_index + 1, right, count+1)
