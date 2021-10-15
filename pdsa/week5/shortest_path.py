import numpy as np


def dijkstra_mtx(wmat, s):
	"""
	Given a wieghted adjacency matrix, finds the shortest paths from the source s to every other vertex using dijkstra's algorithm.
	"""
	
	no_of_rows, no_of_cols, _ = wmat.shape
	infinity = np.max(wmat)*no_of_rows + 1

	visited, distance = dict(), dict()
	for v in range(no_of_rows):
		visited[v] = False
		distance[v] = infinity

	distance[s] = 0
	for u in range(no_of_rows):
		next_vertex_distance = min(distance[v] for v in range(no_of_rows) if not visited[v])
		next_vertex_list = [v for v in range(no_of_rows) if (not visited[v] and distance[v] == next_vertex_distance)]

		if not next_vertex_list:
			break

		next_vertex = min(next_vertex_list)
		visited[next_vertex] = True
		for v in range(no_of_cols):
			if wmat[next_vertex, v, 0] and not visited[v]:
				distance[v] = min([distance[v], distance[next_vertex] + wmat[next_vertex, v, 1]])

	return distance


def dijkstra_list(wlist, s):
	"""
	Given a wieghted adjacency list, finds the shortest paths from the source s to every other vertex using dijkstra's algorithm.
	"""
	
	infinity = len(wlist.keys())*max(d for u in wlist.keys() for _, d in wlist[u]) + 1

	visited, distance = dict(), dict()
	for v in wlist.keys():
		visited[v] = False
		distance[v] = infinity

	distance[s] = 0
	for u in wlist.keys():
		next_vertex_distance = min(distance[v] for v in wlist.keys() if not visited[v])
		next_vertex_list = [v for v in wlist.keys() if (not visited[v] and distance[v] == next_vertex_distance)]

		if not next_vertex_list:
			break

		next_vertex = min(next_vertex_list)
		visited[next_vertex] = True
		for v, d in wlist[next_vertex]:
			if not visited[v]:
				distance[v] = min([distance[v], distance[next_vertex] + d])
	
	return distance


def bellman_ford_mtx(wmtx, s):
	"""
	Given a wieghted adjacency matrix, finds the shortest paths from the source s to every other vertex using bellman-ford algorithm.
	"""

	no_of_rows, no_of_cols, _ = wmtx.shape
	infinity = np.max(wmtx) + 1

	distance = dict()
	for v in range(no_of_rows):
		distance[v] = infinity

	distance[s] = 0

	for _ in range(no_of_rows):
		for u in range(no_of_rows):
			for v in range(no_of_cols):
				if wmat[u, v, 0]:
					distance[v] = min([
						distance[v], distance[u] + wmat[u][v][1]
						])

	return distance


def bellman_ford_list(wlist, s):
	"""
	Given a wieghted adjacency list, finds the shortest paths from the source s to every other vertex using bellman-ford algorithm.
	"""

	infinity = len(wlist.keys())*max(d for u in wlist.keys() for _, d in wlist[u]) + 1

	distance = dict()
	for v in wlist.keys():
		distance[v] = infinity

	distance[s] = 0

	for _ in range(len(wlist.keys())):
		for u in wlist.keys():
			for v, d in wlist[u]:
				distance[v] = min([
					distance[v], distance[u] + d
					])

	return distance


def floyd_warshall(wmat):
	"""
	Given a weighted asjacency matrix, will return a matrix with the lengths of the shortest paths from any pair of vertices.
	"""

	no_of_rows, no_of_cols, _ = wmat.shape
	infinity = np.max(wmat) + 1
	
	sp = np.zeros(shape=(no_of_rows, no_of_cols, no_of_rows+1))
	for i in range(no_of_rows):
		for j in range(no_of_cols):
			sp[i, j, 0] = wmat[i, j, 1] if wmat[i, j, 0] else infinity

	for k in range(no_of_cols):
		for i in range(no_of_rows):
			for j in range(no_of_cols):
				sp[i, j, k+1] = min([
					sp[i, j, k],
					sp[i, k, k] + sp[k, j, k]
					])

	return sp[:, :, -1]


def prim_list(wlist):
	"""
	Finds a minimum cost spanning tree using prim's algorithm.
	"""

	infinity = len(wlist.keys())*max(d for u in wlist.keys() for _, d in wlist[u]) + 1

	visited, distance, tree_edges = dict(), dict(), []
	for v in wlist.keys():
		visited[v] = False
		distance[v] = infinity

	visited[0] = True
	for v, d in wlist[0]:
		distance[v] = d

	for _ in range(len(wlist.keys())):
		min_distance = infinity
		next_vertex = None
		for u in wlist.keys():
			for v, d in wlist[u]:
				if visited[u] and not visited[v] and d < min_distance:
					min_distance = d
					next_vertex = v
					next_edge = (u, v)
		
		if next_vertex is None:
			break

		visited[next_vertex] = True
		tree_edges.append(next_edge)
		for v, d in wlist[next_vertex]:
			if not visited[v]:
				distance[v] = min([distance[v], d])

		return tree_edges


def prim_list2(wlist):

	infinity = len(wlist.keys())*max(d for u in wlist.keys() for _, d in wlist[u]) + 1

	visited, distance, neighbor = dict(), dict(), dict()
	for v in wlist.keys():
		visited[v] = False
		distance[v] = infinity
		neighbor[v] = -1

	for i in range(1, len(wlist.keys())):
		next_vertex_distance = min(distance[v] for v in wlist.keys() if not visited[v])
		next_vertex_list = [v for v in wlist.keys() if (not visited[v] and distance[v] == next_vertex_distance)]

		if not next_vertex_list:
			break

		next_vertex = min(next_vertex_list)
		visited[next_vertex] = True
		for v, d in wlist[next_vertex]:
			if not visited[v]:
				distance[v] = min([distance[v], d])
				neighbor[v] = next_vertex

	return neighbor


def kruskal(wlist):
	"""
	Finds a minimum cost spanning tree using kruskal's algorithm. 
	"""
	
	edges, component_number, tree_edges = [], dict(), []
	for u in wlist.keys():
		edges.extend((d, u, v) for v, d in wlist[u])
		component_number[u] = u

	edges.sort()

	for d, u, v in edges:
		if component_number[u] != component_number[v]:
			tree_edges.append((u, v))
			current_component = component_number[u]
			for w in wlist.keys():
				if component_number[w] == current_component:
					component_number[w] = component_number[v]

	return tree_edges

l = {
	1: [(2, 10), (8, 8)],
	2: [(6, 2)],
	3: [(2, 1), (4, 1)],
	4: [(5, 3)],
	5: [(6, -1)],
	6: [(3, -2)],
	7: [(2, -4), (6, -1)],
	8: [(7, 1)]
}

print(bellman_ford_list(l, 1))