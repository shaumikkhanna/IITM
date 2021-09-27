
def EvaluateExpression(exp):
	stack = []
	for element in exp.split():
		try:
			stack.append(int(element))
		except ValueError:
			b, a = stack.pop(), stack.pop()
			stack.append(eval(f'{a}{element}{b}'))

	return stack[-1]

