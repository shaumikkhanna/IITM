
class Point:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y 

	def move(self, delta_x, delta_y):
		self.x += delta_x
		self.y += delta_y

	def value(self):
		return self.x, self.y 

	def duplicate(self):
		return Point(self.x, self.y)
