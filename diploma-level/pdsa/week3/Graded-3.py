
class Node:

	def __init__(self, value=None):
		self.value = value
		self.next = None

	def isEmpty(self):
		return self.value is None


def reverse(root):
	if root.isEmpty():
		return root

	current_node = root
	prev_node = None
	while current_node is not None:
		next_node, current_node.next = current_node.next, prev_node
		prev_node, current_node = current_node, next_node

	return prev_node



