
class Node:
	def __init__(self, data):
	self.data = data
	self.next = None 
	self.prev = None 


class doubly_linked_list:
  def __init__(self):
	self.head = None 
	self.last = None

  def insert_end(self, data):
	new_node = Node(data)

	if self.head is None:
	  self.head = new_node
	  self.last = new_node 

	elif self.head == self.last:
	  self.head.next = new_node
	  self.last = new_node
	  self.last.prev = self.head

	else:
	  self.last.data, new_node.data = new_node.data, self.last.data
	  self.last.prev.next, new_node.prev = new_node, self.last.prev
	  self.last.prev, new_node.next = new_node, self.last


  def delete_end(self):

	if self.head == self.last:
	  self.head = None 
	  self.last = None 

	elif self.head.next == self.last:
	  self.last = self.head
	  self.head.next = None

	else:
	  self.last.data, self.last.prev.data = self.last.prev.data, self.last.data
	  self.last.prev.prev.next, self.last.prev = self.last, self.last.prev.prev
