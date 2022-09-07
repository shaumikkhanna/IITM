x = float(input())
y = float(input())


if not x and not y:
	print('Origin')
elif not x:
	print('Y-axis')
elif not y:
	print('X-axis')
elif x > 0:
	if y > 0:
		print('I')
	else:
		print('IV')
else:
	if y > 0:
		print('II')
	else:
		print('III')