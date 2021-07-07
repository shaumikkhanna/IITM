
def convertToRecord(filename):
	out = []
	with open(filename, 'r') as f:
		column_names = f.readline().strip().split(',')
		for line in f.readlines():
			my_dict = dict()
			for column_name, value in zip(column_names, line.strip().split(',')):
				try:
					my_dict[column_name] = int(value)
				except ValueError:
					my_dict[column_name] = value
			out.append(my_dict)
	return out
