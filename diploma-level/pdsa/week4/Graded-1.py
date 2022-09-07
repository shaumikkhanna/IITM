
class Queue:

	def __init__(self):
		self.lst = [] 

	def add(self, value):
		self.lst.append(value)

	def pop(self):
		return self.lst.pop(0)

	def isempty(self):
		return not self.lst


def findConnectionLevel(n, Gmat, Px, Py):
	level = [-1 for _ in range(n)]

	q = Queue()
	q.add(Px)
	level[Px] = 0

	while not q.isempty():
		current_vertex = q.pop()
		for neighbor in range(n):
			if Gmat[current_vertex][neighbor]:
				if level[neighbor] == -1:
					level[neighbor] = level[current_vertex]+1
					q.add(neighbor)

	return level[Py]

