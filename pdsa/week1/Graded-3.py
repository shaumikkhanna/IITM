
def odd_one(l):
	a, b = type(l[0]), type(l[1])
	if a == b:
		for el in l[2:]:
			c = type(el)
			if c != a:
				return c.__name__
	else:
		c = type(l[2])
		return a.__name__ if b == c else b.__name__
