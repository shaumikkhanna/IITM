def reverse(input_list):
	if len(input_list) == 1:
		return input_list
	else:
		return input_list[-1:] + reverse(input_list[:-1])