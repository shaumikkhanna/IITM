
class StringManipulation:

	def __init__(self, wlist: list):
		self.wlist = wlist

	def Words_of_length(self, length):
		return [word for word in self.wlist if len(word) == length]

	def Words_starts_with(self, char):
		return [word for word in self.wlist if word.startswith(char)]

	def Words_end_with(self, char):
		return [word for word in self.wlist if word.endswith(char)]

	@staticmethod
	def is_palindrome(word):
		return word == word[::-1]

	def Palindromes(self):
		return [word for word in self.wlist if StringManipulation.is_palindrome(word)]

	def Total_words(self):
		return len(self.wlist)

	def Longest_word(self):
		return max(self.wlist, key=len)

	def Smallest_word(self):
		return min(self.wlist, key=len)

	def Count(self, word):
		return sum(word == word_ for word_ in self.wlist)
