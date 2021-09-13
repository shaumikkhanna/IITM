import math


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

class Line:

	def __init__(self, startPoint: Point, endPoint: Point):
		self.startPoint = startPoint
		self.endPoint = endPoint

	def get_coordinates(self):
		x0, y0 = self.startPoint.value()
		x1, y1 = self.endPoint.value()
		return x0, y0, x1, y1

	def length(self):
		x0, y0, x1, y1 = self.get_coordinates()

		return math.sqrt(
			(x0 - x1)**2 + (y0 - y1)**2
			)

	def slope(self):
		x0, y0, x1, y1 = self.get_coordinates()
		
		try:
			return round((y1 - y0) / (x1 - x0), 2)
		except ZeroDivisionError:
			return math.inf 




