import numpy as np


class Stack:
	""" Depth first search application. """

	def __init__(self):
		self.lst = []

	def add(self, value):
		self.lst.append(value)

	def pop(self):
		if not self.isempty():
			return self.lst.pop()
		else:
			return None

	def isempty(self):
		return not self.lst

	def __str__(self):
		return self.lst.__str__()


class Queue(Stack):
	""" Breadth first search application. """

	def pop(self):
		if not self.isempty():
			return self.list.pop(0)
		else:
			return None


def neighbors(graph_mtx: np.array, i):
	"""Given an adjacency matrix and a vertex i, 
	returns a list of vertices where i connects to."""

	out = []
	no_of_rows, _ = graph_mtx.shape

	for j in range(no_of_rows):
		if graph_mtx[i, j]:
			out.append(j)

	return out


def bfs_mtx(adj_mtx: np.array, i):
	"""Given an adjacency matrix, returns a list 
	describing if a vertex is reachable from i. """

	visited = [False for _ in range(adj_mtx.shape[0])]

	q = Queue()
	visited[i] = True
	q.add(i)

	while not q.isempty():
		current_vertex = q.pop()
		for neighbor in neighbors(adj_mtx, current_vertex):
			if not visited[neighbor]:
				visited[neighbor] = True
				q.add(neighbor)

	return visited
		

def bfs_list_path(adj_list: dict, i):
	visited, parent = [], []
	for vertices in adj_list.keys():
		visited[vertices] = False
		parent[vertices] = -1

	q = Queue()
	visited[i] = True
	q.add(i)

	while not q.isempty():
		current_vertex = q.pop()
		for neighbor in adj_list[current_vertex]:
			if not visited[neighbor]:
				visited[neighbor] = True
				parent[neighbor] = current_vertex
				q.add(neighbor)

	return visited, parent


def bfs_list_path_level(adj_list: dict, i):
	level, parent = [], []
	for vertices in adj_list.keys():
		level[vertices] = -1
		parent[vertices] = -1

	q = Queue()
	level[i] = 0
	q.add(i)

	while not q.isempty():
		current_vertex = q.pop()
		for neighbor in adj_list[current_vertex]:
			if level[neighbor] == -1:
				level[neighbor] = level[current_vertex] + 1
				parent[neighbor] = current_vertex
				q.add(neighbor)

	return visited, parent


def toposort(adj_mtx: np.array):
	indegree = dict()
	out = []
	n, _ = adj_mtx.shape

	for j in range(n):
		indegree[j] = sum(adj_mtx[i][j] for i in range(n))

	for i in range(n):
		j = min([x for x in range(n) if not indegree[x]])
		out.append(j)
		indegree[j] -= 1
		for k in range(n):
			if adj_mtx[j][k]:
				indegree[k] -= 1

	return out


def longest_path_list(adj_list: dict):
	indegree, longest_paths = dict(), dict()
	for u in adj_list.keys():
		indegree[u] = 0
		longest_paths[u] = 0
	for edges in adj_list.values():
		for v in edges:
			indegree[v] += 1

	zero_degree_queue = Queue()
	for u in adj_list.keys():
		if not indegree[u]:
			zero_degree_queue.add(u)

	while not zero_degree_queue.isempty():
		j = zero_degree_queue.pop()
		indegree[j] -= 1

		for k in adj_list[j]:
			indegree[k] -= 1
			longest_paths[k] = max((longest_paths[k], longest_paths[j] + 1))
			if not indegree[k]:
				zero_degree_queue.add(k)

	return longest_paths











