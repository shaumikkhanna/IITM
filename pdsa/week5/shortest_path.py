import numpy as np


### SINGLE SOURCE SHORTEST PATH ALGORITHMS

def dijkstra_mtx(wmat, s):
	"""
	Given a weighted adjacency matrix, finds the shortest 
	paths from the source s to every other vertex using 
	dijkstra's algorithm (fire algorithm). This alsorithm
	does not allow for negative weights.
	"""
	
	no_of_rows, no_of_cols, _ = wmat.shape
	infinity = np.max(wmat)*no_of_rows + 1

	# Initialisation; here, distance is the upper bound 
	# for the time to burn from the source.
	visited, distance = dict(), dict()
	for v in range(no_of_rows):
		visited[v] = False
		distance[v] = infinity

	distance[s] = 0
	for _ in range(no_of_rows):

		# Find next vertex with minimum distance
		next_vertex_distance = min(distance[v] for v in range(no_of_rows) if not visited[v])
		next_vertex_list = [v for v in range(no_of_rows) if (not visited[v] and distance[v] == next_vertex_distance)]
		if not next_vertex_list:
			break
		next_vertex = min(next_vertex_list)

		# Update expected time to burn of neighbors of next_vertex 
		visited[next_vertex] = True
		for v in range(no_of_cols):
			if wmat[next_vertex, v, 0] and not visited[v]:
				distance[v] = min([distance[v], distance[next_vertex] + wmat[next_vertex, v, 1]])

	return distance


def dijkstra_list(wlist, s):
	"""
	Given a weighted adjacency list, finds the shortest 
	paths from the source s to every other vertex using 
	dijkstra's algorithm (fire algorithm). This alsorithm
	does not allow for negative weights.
	"""
	
	infinity = len(wlist.keys())*max(d for u in wlist.keys() for _, d in wlist[u]) + 1

	# Initialisation; here, distance is the upper bound 
	# for the time to burn from the source.
	visited, distance = dict(), dict()
	for v in wlist.keys():
		visited[v] = False
		distance[v] = infinity

	distance[s] = 0
	for _ in range(len(wlist.keys())):

		# Find next vertex with minimum distance
		next_vertex_distance = min(distance[v] for v in wlist.keys() if not visited[v])
		next_vertex_list = [v for v in wlist.keys() if (not visited[v] and distance[v] == next_vertex_distance)]
		if not next_vertex_list:
			break
		next_vertex = min(next_vertex_list)

		# Update expected time to burn of neighbors of next_vertex 
		visited[next_vertex] = True
		for v, d in wlist[next_vertex]:
			if not visited[v]:
				distance[v] = min([distance[v], distance[next_vertex] + d])
	
	return distance


def bellman_ford_mtx(wmtx, s):
	"""
	Given a weighted adjacency matrix, finds the shortest paths 
	from the source s to every other vertex using bellman-ford 
	algorithm. Weights need not be positive but there must not
	be any negative weight cycle.
	"""

	no_of_rows, no_of_cols, _ = wmtx.shape
	infinity = np.max(wmtx) + 1

	# Initialisation
	distance = dict()
	for v in range(no_of_rows):
		distance[v] = infinity

	distance[s] = 0

	for _ in range(no_of_rows):
		# Repeat n times till stable
		for u in range(no_of_rows):
			for v in range(no_of_cols):
				if wmat[u, v, 0]:
					
					# For every edge u, v
					distance[v] = min([
						distance[v], distance[u] + wmat[u][v][1]
						])

	return distance


def bellman_ford_list(wlist, s):
	"""
	Given a weighted adjacency list, finds the shortest paths 
	from the source s to every other vertex using bellman-ford 
	algorithm. Weights need not be positive but there must not
	be any negative weight cycle.
	"""

	infinity = len(wlist.keys())*max(d for u in wlist.keys() for _, d in wlist[u]) + 1

	# Initialisation
	distance = dict()
	for v in wlist.keys():
		distance[v] = infinity

	distance[s] = 0

	for _ in range(len(wlist.keys())):
		# Repeat n times
		for u in wlist.keys():
			for v, d in wlist[u]:
				# For every edge u, v

				distance[v] = min([
					distance[v], distance[u] + d
					])

	return distance


### ALL PAIRS SHORTEST PATH ALGORITHMS


def floyd_warshall(wmat):
	"""
	Given a weighted adjacency matrix, will return a matrix with the lengths of the shortest paths from any pair of vertices.
	"""

	no_of_rows, no_of_cols, _ = wmat.shape
	infinity = np.max(wmat) + 1
	
	# Initialisation of shortest path matrix
	sp = np.zeros(shape=(no_of_rows, no_of_cols, no_of_rows+1))
	for i in range(no_of_rows):
		for j in range(no_of_cols):
			sp[i, j, 0] = wmat[i, j, 1] if wmat[i, j, 0] else infinity

	for k in range(no_of_cols):
		# kth stage of shortest path matrix

		for i in range(no_of_rows):
			for j in range(no_of_cols):

				# For all i, j update shortest path matrix
				sp[i, j, k+1] = min([
					sp[i, j, k],
					sp[i, k, k] + sp[k, j, k]
					])

	return sp[:, :, -1]


### MINIMUM COST SPANNING TREES ALGORITHMS


def prim_list(wlist):
	"""
	Finds a minimum cost spanning tree using prim's algorithm.
	"""

	infinity = len(wlist.keys())*max(d for u in wlist.keys() for _, d in wlist[u]) + 1

	# Initialisation; here, distance means distance of vertex 
	# from all vertices already in the tree.
	tree_visited, tree_edges = dict(), []
	distance = dict()
	for v in wlist.keys():
		tree_visited[v] = False
		distance[v] = infinity

	tree_visited[0] = True
	for v, d in wlist[0]:
		distance[v] = d

	for _ in range(len(wlist.keys())):
		
		# Find lowest cost edge u, v where u in tree and v not in tree.
		min_distance = infinity
		next_vertex = None
		for u in wlist.keys():
			for v, d in wlist[u]:
				if tree_visited[u] and not tree_visited[v] and d < min_distance:
					min_distance = d
					next_vertex = v
					next_edge = (u, v)
		
		# If graph is disconnected
		if next_vertex is None:
			break

		tree_visited[next_vertex] = True
		tree_edges.append(next_edge)

		# Update the distances of the neighbors of next_vertex.
		for v, d in wlist[next_vertex]:
			if not tree_visited[v]:
				distance[v] = min([distance[v], d])

		return tree_edges


def prim_list2(wlist):
	"""
	This is a better implementation of the prim_list function.
	"""

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
	
	# Initialisation
	tree_edges, component_number = [], dict()
	edges = []
	for u in wlist.keys():
		edges.extend((d, u, v) for v, d in wlist[u])
		component_number[u] = u

	# Sort edges by weight
	edges.sort()

	for _, u, v in edges:
		if component_number[u] != component_number[v]:
			tree_edges.append((u, v))

			# Update component number of all vertices connected to u.
			current_component = component_number[u]
			for w in wlist.keys():
				if component_number[w] == current_component:
					component_number[w] = component_number[v]

	return tree_edges


