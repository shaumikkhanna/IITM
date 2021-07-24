def is_perfect(selection):
	all_selected = list(selection.values())
	return len(all_selected) == len(set(all_selected))
