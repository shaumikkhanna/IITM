
class Hashing:

	def __init__(self, c1, c2, m):
		self.hashtable = [None for _ in range(m)]
		self.c1 = c1
		self.c2 = c2
		self.m = m

	def store_data(self, data):
		h = self.hash_function()

		for i in range(self.m):
			index = h(data, i)
			if self.hashtable[index] is None:
				self.hashtable[index] = data
				return
				
		print('Hash table is full')

	def hash_function(self):
		return lambda k, i: (k + self.c1*i + self.c2*i**2) % m

	def display_hashtable(self):
		return self.hashtable



