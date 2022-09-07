
def DishPrepareOrder(order_list):
	order_freq = dict()
	for order_number in order_list:
		try:
			order_freq[order_number] += 1
		except KeyError:
			order_freq[order_number] = 1

	return sorted(order_freq.keys(), key=lambda x: (order_freq[x], -x), reverse=True)
