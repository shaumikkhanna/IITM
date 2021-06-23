x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())


try:
	slope = (y_2 - y_1) / (x_2 - x_1)
	linetype = 'Horizontal Line' if not slope else 'Positive Slope' if slope > 0 else 'Negative Slope'

	print(y_1 + slope*(x_3 - x_1))
	print(linetype)
	
except ZeroDivisionError:
	print('Vertical Line')