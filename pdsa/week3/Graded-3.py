# Not completed


class Node:

	def __init__(self, value=None):
		self.value = value
		self.next = None

	def isEmpty(self):
		return self.value is None

	def __str__(self):
		return f'n{self.value}'


def reverse(root):
	if root.isEmpty():
		return root

	nodes = []
	temp_node = root
	while temp_node is not None:
		nodes.append(temp_node)
		temp_node = temp_node.next

	for node in nodes:
		print(node)

	temp_last_node = nodes.pop()
	while nodes:
		new_node = nodes.pop()
		temp_last_node.next = new_node
		temp_last_node = temp_last_node.next


l = Node(1)
l.next = Node(2)
l.next.next = Node(3)
l.next.next.next = Node(4)


