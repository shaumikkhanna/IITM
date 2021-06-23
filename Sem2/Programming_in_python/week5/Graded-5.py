def process():
	while True:
		min_1 = board_min()
		board_erase(min_1)
		
		if board_isEmpty():
			return min_1
		
		min_2 = board_min()
		board_erase(min_2)
		
		board_write(abs(min_1-min_2))