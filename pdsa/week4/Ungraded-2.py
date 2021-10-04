
def findAllPaths(vertices, adj_list, source, destination):
	all_routes = [source]
	finished_routes = []

	while all_routes:
		updated_routes = []
		for route in all_routes:
			
			for neighbor in adj_list[route[-1]]:
				if neighbor in route:
					continue

				if neighbor == destination:
					finished_routes.append(route + destination)
				else:
					updated_routes.append(route + neighbor)
		
		all_routes = updated_routes

	return finished_routes

