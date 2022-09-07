
def quicksort(lst, left=0, right=None):
	""" This function uses quicksort to sort in place
	lst[left:right] """

	if right is None:
		right = len(lst)

	if right - left <= 1:
		return lst

	pivot = lst[left]
	lower_ind = upper_ind = left + 1

	for i in range(left + 1, right):
		
		if lst[i] > pivot: # Extend the upper section
			upper_ind += 1
		
		else: # Exchange with start of upper section and then shift the sections
			lst[i], lst[lower_ind] = lst[lower_ind], lst[i]
			lower_ind += 1
			upper_ind += 1

	# Move the pivot to inbetween the lower and the upper sections
	lst[left], lst[lower_ind - 1] = lst[lower_ind - 1], lst[left]
	lower_ind -= 1

	quicksort(lst, left, lower_ind)
	quicksort(lst, lower_ind + 1, right)

	return lst


