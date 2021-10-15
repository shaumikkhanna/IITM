
def take_input():
	maze = []
	while True:
		input_ = input().replace('\n', '')
		if not input_:
			break
		else:
			maze.append(input_)

	return maze


def create_adj_list(maze):
	height, width = len(maze), len(maze[0])
	adj_list = dict()

	for i in range(1, height-1):

		# Check for source
		if maze[i][0] != 'X':
			source = (i, 0)
			adj_list[(i, 0)] = [(i, 1)]

		# Check for key
		if maze[i][width-1] == '*':
			key = (i, width-1)
			adj_list[(i, width-1)] = [(i, width-2)]

		# Check for destination
		if maze[i][width-1] != 'X':
			destination = (i, width-1)
			adj_list[(i, width-1)] = [(i, width-2)]
		

		for j in range(1, width-1):
			if maze[i][j] == 'X':
				continue

			if maze[i][j] == '*':
				key = (i, j)

			accessible = []
			
			# North
			if maze[i-1][j] != 'X':
				accessible.append((i-1, j))
			# South
			if maze[i+1][j] != 'X':
				accessible.append((i+1, j))
			# East
			if maze[i][j+1] != 'X':
				accessible.append((i, j+1))
			# West
			if maze[i][j-1] != 'X':
				accessible.append((i, j-1))

			if accessible:
				adj_list[(i, j)] = accessible


	return adj_list, source, key, destination


class Queue:
	def __init__(self):
		self.lst = []

	def add(self, value):
		self.lst.append(value)

	def pop(self):
		return self.lst.pop(0)

	def isempty(self):
		return not self.lst

	def __str__(self):
		return self.lst.__str__()


def bfs_shortest_path(adj_list, a, b):
	level = dict((i, -1) for i in adj_list.keys())

	q = Queue()
	q.add(a)
	level[a] = 0

	while not q.isempty():
		current_vertex = q.pop()
		for neighbor in adj_list[current_vertex]:
			if level[neighbor] == -1:
				level[neighbor] = level[current_vertex] + 1
				q.add(neighbor)

	return level[b]


def main():
	maze = take_input()
	adj_list, source, key, destination = create_adj_list(maze)

	from_source_to_key = bfs_shortest_path(adj_list, source, key)
	if from_source_to_key == -1:
		return -1

	from_key_to_destination = bfs_shortest_path(adj_list, key, destination)
	if from_key_to_destination == -1:
		return -2

	return from_source_to_key + from_key_to_destination


print(main())
