def findMasterTank(v, e):
    master_node = 0
    adj_lst = {k:[] for k in v}
    end_nodes = []
    for edge in e:
        adj_lst[edge[0]].append(edge[1])
        end_nodes.append(edge[1])
    start_node = list(set(v) - set(end_nodes))
    if len(start_node) != 0:
        vertex = start_node[0]
        visited = {k:False for k in v}
        queue = [vertex]
        visited[vertex] = True
        while len(queue) != 0:
            nbs = queue.pop(0)
            for node in adj_lst[nbs]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)
        if all(visited.values()):
            master_node = vertex
    return master_node
    
v = [item for item in input().split(" ")]
#Tanks(vertices) numbered from 1 to n in string format.
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
  s = input().split(" ")
  e.append((s[0], s[1]))
print(findMasterTank(v, e))
