def max_element(input_list):
	if len(input_list) == 1:
		return input_list[0]
	
	first = input_list[0]
	max_others = max_element(input_list[1:])
	return first if first > max_others else max_others
