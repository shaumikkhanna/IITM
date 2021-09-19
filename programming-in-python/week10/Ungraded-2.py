
class StudentResult:

	def __init__(self, *info):
		self.info = info

	def Display(self):
		print(' '.join(self.info))
