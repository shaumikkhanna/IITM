
def FiberLink(distance_map):
	
	# Initialisation for kruskal's alogrithm
	total_fiber_length = 0
	component_number = dict()
	weight = dict()
	edges = []
	for u in range(size):
		for v, d in distance_map[u]:
			edges.append((d, u, v))
			weight[(u, v)] = d
		component_number[u] = u

	edges.sort()

	for d, u, v in edges:
		if component_number[u] == component_number[v]:
			continue

		total_fiber_length += weight[(u, v)]

		current_component = component_number[u]
		for w in distance_map.keys():
			if component_number[w] == current_component:
				component_number[w] = component_number[v]

	return total_fiber_length

