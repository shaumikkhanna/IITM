my_list = [
	a,
	b,
	c,
	a.intersection(b),
	b.intersection(c),
	c.intersection(a),
	a.intersection(b, c),
	a.union(b, c),
	a.intersection(b).difference(c),
	a.intersection(c).difference(b),
	b.intersection(c).difference(a),
	a.difference(b.union(c)),
	b.difference(c.union(a)),
	c.difference(a.union(b))
]

for x in my_list:
	print(f'{len(x)},{round(len(x)/len(my_list[7]), 1)}')