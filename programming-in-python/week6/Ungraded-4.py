def min_dict_key(data):
	return min(data.keys())

def max_dict_key(data):
	return max(data.keys())

def min_value_dict_key(data):
	return min(data.items(), key=lambda x: x[1])[0]

def max_value_dict_key(data):
	return max(data.items(), key=lambda x: x[1])[0]

def sort_by_key(data, order='asc'):
	return dict(sorted(data.items(), key=lambda x: x[0], reverse=order!='asc'))

def sort_by_value(data, order='asc'):
	return dict(sorted(data.items(), key=lambda x: x[1], reverse=order!='asc'))