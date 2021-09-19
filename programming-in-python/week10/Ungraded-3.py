
class StudentResult:

	Count = 0

	def __init__(self, roll, name, math, physics, chemistry, computer, english, email='Not provided'):
		StudentResult.Count += 1

		self.roll = roll 
		self.Student_name = name
		self.marks = {
			'math': math,
			'physics':physics,
			'chemistry': chemistry,
			'computer': computer,
			'english': english
		}
		self.email = email

	def Average_marks(self):
		return sum(self.marks.values()) / 5

	def Total_marks(self):
		return f'{sum(self.marks.values())}/500'

	def Max_marks(self):
		return max(self.marks.values())

	def Min_marks(self):
		return min(self.marks.values())

