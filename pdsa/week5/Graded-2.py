
def djikstra(wlist, a, b):
	infinity = len(wlist.keys())*max(d for u in wlist.keys() for _, d in wlist[u]) + 1

	visited, distance, parent = dict(), dict(), dict()
	for v in wlist.keys():
		visited[v] = False
		distance[v] = infinity
		parent[v] = None

	distance[a] = 0
	for u in wlist.keys():
		next_vertex_distance = min(distance[v] for v in wlist.keys() if not visited[v])
		next_vertex_list = [v for v in wlist.keys() if (not visited[v] and distance[v] == next_vertex_distance)]
		if not next_vertex_list:
			break
		next_vertex = min(next_vertex_list)

		visited[next_vertex] = True
		for v, d in wlist[next_vertex]:
			if not visited[v]:
				if distance[v] > distance[next_vertex] + d:
					distance[v] = distance[next_vertex] + d
					parent[v] = next_vertex

	path = [b]
	while True:
		current_parent = parent[path[-1]]
		if current_parent is None:
			return distance[b], path[::-1]
		else:
			path.append(current_parent)


def min_cost_walk(wlist, source, destination, via):
	
	distance_a, path_a = djikstra(wlist, source, via)
	distance_b, path_b = djikstra(wlist, via, destination)

	return distance_a + distance_b, path_a + path_b[1:]



