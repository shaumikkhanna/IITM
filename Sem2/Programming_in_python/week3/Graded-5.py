phone_no = input()


from string import digits


truth = all(number in digits for number in phone_no) and\
	phone_no[0] in '6789' and\
	len(phone_no) == 10 and\
	all(5*digit not in phone_no for digit in digits) and\
	all(phone_no.count(digit) <= 7 for digit in digits)

print('valid' if truth else 'invalid')