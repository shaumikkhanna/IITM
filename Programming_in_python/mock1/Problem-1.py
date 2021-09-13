chars = input()

out = []
for char1 in chars:
	for char2 in chars:
		for char3 in chars:
			out.append(f'{char1}{char2}{char3}')

print('\n'.join(sorted(out)))

