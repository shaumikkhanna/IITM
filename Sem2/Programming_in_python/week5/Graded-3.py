def check_leap_year(year):
	if year % 4:
		return False
	if year % 100:
		return True
	if year % 400:
		return False
	return True