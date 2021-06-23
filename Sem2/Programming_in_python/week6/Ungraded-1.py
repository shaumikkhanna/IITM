def shift_a_person(order_list, position=1):
	try:
		person = order_list.pop(position - 1)
	except IndexError:
		person = order_list.pop(0)
	order_list.append(person)

	for person in set(order_list):
		for _ in range(order_list.count(person)-1):
			order_list.remove(person)

	return order_list