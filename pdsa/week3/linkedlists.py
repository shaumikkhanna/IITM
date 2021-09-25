
class Node:

	def __init__(self, value=None):
		self.value = value
		self.next = None

	def isempty(self):
		return self.value is None

	def append(self, v):
		if self.isempty():
			self.value = v
		
		temp_last_node = self
		while temp_last_node.next is not None:
			temp_last_node = temp_last_node.next

		temp_last_node.next = Node(v)

	def insert(self, v):
		if self.isempty():
			self.value = v

		new_node = Node(v)

		self.value, new_node.value = new_node.value, self.value
		self.next, new_node.next = new_node, self.next

	def remove(self, v):
		if self.isempty():
			return

		if self.value == v:
			if self.next is not None:
				self.value = self.next.value
				self.next = self.next.next
			else:
				self.value = None

		else:
			if self.next is not None:
				self.next.remove(v)
				if self.next.value is None:
					self.next = None

	def remove_iterating(self, v):
		if self.isempty():
			return

		if self.value == v:
			self.value = self.next.value
			self.next = self.next.next
			return

		temp_node = self
		while temp_node.next is not None:
			if temp_node.next.value == v:
				temp_node.next.value = None
				temp_node.next = temp_node.next.next
				return
			temp_node = temp_node.next


