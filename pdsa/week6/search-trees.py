
class Tree:

	def __init__(self, value=None):
		self.value = value
		if self.value is not None:
			self.right = Tree()
			self.left = Tree()
		else:
			self.right = None 
			self.left = None

	def isempty(self):
		return self.value is None

	def isleaf(self):
		return (
			not self.is_empty() and\
			self.left is None and\
			self.right is None
			)

	def inorder(self):
		if self.isempty():
			return []
		else:
			return self.left.inorder() + [self.value] + self.right.inorder()

	def __str__(self):
		return str(self.inorder())

	def find(self, v):
		if self.is_empty():
			return False

		if v < self.value:
			return self.left.find(v)
		elif v > self.value:
			return self.right.find(v)
		else:
			return True

	def minval(self):
		if self.left.isempty():
			return self.value
		else:
			return self.left.minval()

	def maxval(self):
		if self.right.isempty():
			return self.value
		else:
			return self.right.maxval()

	def insert(self, v):
		if self.isempty():
			self.value = v
			self.left = Tree()
			self.right = Tree()

		if v < self.value:
			self.left.insert(v)
		elif v > self.value:
			self.right.insert(v)

	def delete(self, v):
		if self.isempty():
			return

		if v < self.value:
			return self.left.delete(v)
		elif v > self.value:
			return self.right.delete(v)
		else:
			if self.isleaf():
				self.makeempty()
			elif self.left.isempty():
				self.copyright()
			elif self.right.isempty():
				self.copyleft()
			else:
				self.value = self.left.maxval()
				self.left.delete(self.left.maxval())

	def makeempty(self):
		self.value = None
		self.left = None
		self.right = None

	def copyright(self):
		self.value = self.right.value
		self.left = self.right.left
		self.right = self.right.right

	def copyleft(self):
		self.value = self.left.value
		self.left = self.left.left
		self.right = self.left.right

	








