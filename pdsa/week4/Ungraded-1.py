
class Stack:
	def __init__(self):
		self.lst = []

	def add(self, value):
		self.lst.append(value)

	def pop(self):
		return self.lst.pop()

	def isempty(self):
		return not self.lst

	def __str__(self):
		return self.lst.__str__()


def findComponents_undirectedGraph(vertices, edges):
	
	# Initialisation
	component_number = 0
	visited, adj_list = dict(), dict()
	for v in vertices:
		visited[v] = False
		adj_list[v] = []

	# Construct adjacency list
	for edge in edges:
		i, j = edge
		adj_list[i].append(j)
		adj_list[j].append(i)

	stack = Stack()
	while True:
		# Next component
		try:
			stack.add(min([v for v in vertices if not visited[v]]))
			component_number += 1
		except ValueError:
			return component_number

		# Run dfs for current component
		while not stack.isempty():
			current_vertex = stack.pop()
			visited[current_vertex] = True
			for neighbor in adj_list[current_vertex]:
				if not visited[neighbor]:
					stack.add(neighbor)



### Testing

vertices = [1, 2, 3, 4, 5, 6, 7, 8]
edges = [
	(1, 3),
	(3, 4),
	(3, 7),
	(5, 6),
	(5, 8),
	(6, 8),
	]

print(findComponents_undirectedGraph(vertices, edges))
