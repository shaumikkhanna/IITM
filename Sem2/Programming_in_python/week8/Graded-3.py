def simple_sort(item_list):
	return sorted(item_list)

def simple_search(item_list, item):
	middle_ind = len(item_list) // 2
	if not middle_ind:
		return False
	middle = item_list[middle_ind]
	if middle == item:
		return True
	elif item < middle:
		return simple_search(item_list[:middle_ind], item)
	else:
		return simple_search(item_list[middle_ind+1:], item)
