my_string = input().lower()


from string import ascii_lowercase 


out = ''
for letter in ascii_lowercase:
	out += letter * my_string.count(letter)

print(out)