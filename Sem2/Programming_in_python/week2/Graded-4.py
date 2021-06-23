my_string = input()

out = set(letter for letter in my_string if letter in 'aeiou')
print(''.join(sorted(out)))