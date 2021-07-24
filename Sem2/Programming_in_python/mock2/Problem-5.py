
class Book:

	def __init__(self, name, author, pages, genre):
		self.name = name
		self.author = author
		self.pages = pages
		self.genre = genre

	def is_fiction(self):
		return self.genre == 'Fiction'

	def is_nonFiction(self):
		return self.genre == 'Nonfiction'

	def time_to_read(self):
		if self.pages < 100:
			return '5 days'
		elif self.pages <= 500:
			return '20 days'
		else:
			return 'infinite'

	def same_author(self, other):
		return self.author == other.author
