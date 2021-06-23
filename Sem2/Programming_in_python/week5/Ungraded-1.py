def solve(eq1, eq2):
	a1, b1, c1 = eq1
	a2, b2, c2 = eq2
	denom = (a1*b2 - a2*b1) *(-1)
	x1 = (c1*b2 - c2*b1) // denom
	x2 = (a1*c2 - a2*c1) // denom
	return x1, x2