def listToDict(my_list):
	out = {}
	for ind, lst in enumerate(my_list):
		out[ind] = dict(zip(range(len(lst)), lst))
	return out 

def dictToList(my_dict):
	length = max(my_dict.keys()) + 1
	inner_length = max(max(d.keys()) for d in my_dict.values()) + 1
	out = [[0 for _ in range(inner_length)] for _ in range(length)]
	
	for ind, d in my_dict.items():
		for k, v in d.items():
			out[ind][k] = v

	return out

dictToList({1:{5:1, 2:9}, 3:{0:1}})