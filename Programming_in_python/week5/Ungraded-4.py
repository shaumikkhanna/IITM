def pearson_correlation(x, y):
	n_x = len(x)
	n_y = len(y)

	if n_x != n_y:
		return 0.0

	x_bar = sum(x) / n_x
	y_bar = sum(y) / n_y

	sum_of_mixed_deviaition = sum((x[i] - x_bar)*(y[i] - y_bar) for i in range(n_x))
	sum_of_squared_deviation_x = sum((x0 - x_bar)**2 for x0 in x)
	sum_of_squared_deviation_y = sum((y0 - y_bar)**2 for y0 in y)

	return f'{sum_of_mixed_deviaition / (sum_of_squared_deviation_x*sum_of_squared_deviation_y)**(0.5):.1f}'
