class Infinity:

	def __lt__(self, other):
		return False

	def __gt__(self, other):
		return True

	def __eq__(self, other):
		return False


class XYZ_Courier:

	def __init__(self, wlist):
		self.wlist = wlist

	def route(self, source, destination):
		infinity = Infinity()
		
		visited, cost, parent = dict(), dict(), dict()
		for v in self.wlist.keys():
			visited[v] = False
			cost[v] = infinity
			parent[v] = None

		cost[source] = 0
		for _ in range(len(self.wlist.keys())):
			next_vertex_cost = min(cost[v] for v in self.wlist.keys() if not visited[v])
			next_vertex_list = [v for v in self.wlist.keys() if (not visited[v] and cost[v] == next_vertex_cost)]
			if not next_vertex_list:
				break

			next_vertex = min(next_vertex_list)
			visited[next_vertex] = True
			for v, d in self.wlist[next_vertex]:
				if not visited[v] and cost[v] > cost[next_vertex] + d:
					cost[v] = cost[next_vertex] + d
					parent[v] = next_vertex

		route = [destination]
		while True:
			current_parent = parent[route[-1]]
			if current_parent is None:
				return route[::-1]
			else:
				route.append(current_parent)

	def cost(self, source, destination):
		infinity = Infinity()
		
		visited, cost = dict(), dict()
		for v in self.wlist.keys():
			visited[v] = False
			cost[v] = infinity

		cost[source] = 0
		for _ in range(len(self.wlist.keys())):
			next_vertex_cost = min(cost[v] for v in self.wlist.keys() if not visited[v])
			next_vertex_list = [v for v in self.wlist.keys() if (not visited[v] and cost[v] == next_vertex_cost)]
			if not next_vertex_list:
				break

			next_vertex = min(next_vertex_list)
			visited[next_vertex] = True
			for v, d in self.wlist[next_vertex]:
				if not visited[v]:
					cost[v] = min([
						cost[v],
						cost[next_vertex] + d
						])

		return 5 * cost[destination]

