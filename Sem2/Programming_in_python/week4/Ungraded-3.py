my_string = input()


from string import digits, ascii_lowercase


out = ''
for letter in my_string:
	if letter == ' ':
		out += '_'
	elif letter.isdigit():
		out += digits[::-1][digits.index(letter)]
	elif letter.isalpha():
		uppercase = letter.isupper()
		alphabet = ascii_lowercase[::-1][ascii_lowercase.index(letter.lower())]
		if letter.isupper():
			out += alphabet.upper()
		else:
			out += alphabet
	else:
		out += letter

print(out)
