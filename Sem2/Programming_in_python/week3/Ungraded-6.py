base_string = input()
my_string = input()


for letter in set(base_string):
	my_string = my_string.replace(letter, '')

print(my_string)