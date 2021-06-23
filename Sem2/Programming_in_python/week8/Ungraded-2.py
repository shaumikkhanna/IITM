def isBlock(nodes):
	x, y = min(nodes, key=sum)
	return all(node in nodes for node in [
		(x + 1, y),
		(x, y + 1),
		(x + 1, y + 1)
		])
