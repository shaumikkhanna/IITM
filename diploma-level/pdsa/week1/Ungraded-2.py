from math import sqrt


class Triangle:

	def __init__(self, a, b, c):
		self.a = a 
		self.b = b
		self.c = c 

	def is_valid(self):
		if all([
			self.a + self.b > self.c,
			self.b + self.c > self.a,
			self.a + self.c > self.b
				]):
			return 'Valid'
		else:
			return 'Invalid'

	def Side_Classification(self):
		if self.is_valid() == 'Invalid':
			return 'Invalid'

		if self.a == self.b == self.c:
			return 'Equilateral'
		elif self.a != self.b != self.c and self.a != self.c:
			return 'Scalene'
		else:
			return 'Isosceles'

	def Angle_Classification(self):
		if self.is_valid() == 'Invalid':
			return 'Invalid'

		a, b, c = sorted([self.a, self.b, self.c])

		lhs = a ** 2 + b ** 2
		rhs = c ** 2

		if lhs > rhs:
			return 'Acute'
		elif lhs == rhs:
			return 'Right'
		else:
			return 'Obtuse'

	def Area(self):
		if self.is_valid() == 'Invalid':
			return 'Invalid'

		s = (self.a + self.b + self.c) / 2
		return sqrt(s*(s-a)*(s-b)*(s-c))




