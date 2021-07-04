log = {'S': 0, 'C': 0, 'W': 0, 'O': 0}

tickets_sold_so_far = 0
while True:
	input_ = input()
	if not input_:
		break
	time, *booking = input_.split()
	
	hour, minute = int(time[:2]), int(time[3:])
	if hour < 10:
		continue # Early
	if hour >= 17 and not minute:
		continue # Late

	identifiers, current_tickets = [], []
	while booking:
		identifiers.append(booking.pop(0))
		current_tickets.append(int(booking.pop(0)))
	
	total_tickets_in_booking = sum(current_tickets)
	if tickets_sold_so_far + total_tickets_in_booking <= 100:
		tickets_sold_so_far += total_tickets_in_booking
		for identifier, ticket in zip(identifiers, current_tickets):
			log[identifier] += ticket
