my_string = input()

out = ''
for letter in my_string:
	if letter.isalpha():
		continue
	elif letter in ['{', '[', '(']:
		out += letter
	else:
		if letter == '}': opening = '{'
		if letter == ']': opening = '['
		if letter == ')': opening = '('

		if out[-1] == opening:
			out = out[:-1]
		else:
			print(False)
			break

else:
	print(not out)
