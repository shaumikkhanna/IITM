from string import digits

def commaLineToList(line):
	
	# Splitting the string
	my_list = []
	line = list(line)
	my_string = ''
	while line:
		char = line.pop(0)
		if char == ',':
			my_list.append(my_string)
			my_string = ''
		elif char == '"':
			char = line.pop(0)
			while char != '"':
				my_string += char
				char = line.pop(0)
		else:
			my_string += char
	my_list.append(my_string)

	# Formatting the strings in the list
	out = []
	for el in my_list:
		el = el.strip()

		# For movie collection figure
		if el[0] == '$':
			out.append(
				int(float(el.replace('$', '').replace('M', '')) * 10**6)
				)
			continue

		# For numbers
		numbers_syntax = digits + ',.'
		if all(digit in numbers_syntax for digit in el):
			el = el.replace(',', '')
			if '.' in el:
				out.append(float(el))
			else:
				out.append(int(el))
			continue

		# Otherwise
		out.append(el)

	return out


input_ = """66,3 Idiots,2009,170 ,"Comedy, Drama",8.4,67,"Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them ""idiots"".","354,804",$6.53M"""
print(commaLineToList(input_))

