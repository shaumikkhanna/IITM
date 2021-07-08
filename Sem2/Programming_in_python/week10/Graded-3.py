
class TimeConverter:

	def __init__(self, seconds):
		self.seconds = seconds

	def Second_to_Minutes(self):
		total = self.seconds
		minutes = total // 60
		total -= 60 * minutes
		seconds = total
		return '{} min {} sec'.format(minutes, seconds)

	def Second_to_Hours(self):
		total = self.seconds
		hours = total // 3600
		total -= 3600 * hours
		minutes = total // 60
		total -= 60 * minutes
		seconds = total
		return '{} hr {} min {} sec'.format(hours, minutes, seconds)

	def Second_to_Days(self):
		total = self.seconds
		days = total // 86400
		total -= 86400 * days
		hours = total // 3600
		total -= 3600 * hours
		minutes = total // 60
		total -= 60 * minutes
		seconds = total
		return '{} days {} hr {} min {} sec'.format(days, hours, minutes, seconds)

