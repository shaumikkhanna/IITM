password = input()

print(
	8 <= len(password) <= 32 and\
	password[0].isalpha() and\
	all(char not in password for char in ' /\\"\'')
	)